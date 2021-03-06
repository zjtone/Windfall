from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.course import CourseSerializer, CourseUserRefSerializer
from assistant.api.v1.serializers.order import OrderSerializer, OrderRefSerializer
from assistant.db import course, order, shopping, people
from assistant.api.apiviews import MyAPIView
from assistant.models import OrderRef


class OrderApi(MyAPIView):
    def get(self, request):
        params = request.data
        if 'order_id' not in params or 'org_id' not in params:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        user_order = order.get_order(params["order_id"])
        order_list = order.get_order_ref_by_order_id(params["order_id"])
        course_ids = []
        for good in order_list:
            if good.type == OrderRef.Type.COURSE.value:
                # 课程
                course_ids.append(good.good_id)
        return Response({
            "courses": CourseSerializer(course.list_course_by_id(course_ids), many=True).data,
            "pay_time": user_order.pay_time
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        @api {post} /order/ create order
        @apiName CreateOrder
        @apiGroup Order
        @apiParam {Number} user_id
        @apiParam {Number} org_id
        @apiParam {Array} data
        @apiParamExample {json} Request-Example:
        {
            "user_id": 1,
            "org_id": 1,
            "data": [
                {"good_id": 1, "type": 1, "price": 0, "count": 1},
                {"good_id": 2, "type": 0, "price": 0, "count": 1}
            ]
        }
        """
        params = request.data
        if "user_id" not in params or "org_id" not in params \
                or "data" not in params or not isinstance(params["data"], list) \
                or len(params["data"]) == 0 or len(params["data"]) > 10:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            save_point = transaction.savepoint()
            # 创建订单
            order_serializer = OrderSerializer(data={"user_id": params["user_id"], "org_id": params["org_id"]})
            if order_serializer.is_valid():
                order_serializer.save()
            else:
                transaction.savepoint_rollback(save_point)
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # 订单中增加商品
            for good in params["data"]:
                count = 1
                if "count" in params:
                    count = int(params["count"])

                # 不能超过课程容量
                if good["type"] == 0:
                    tmp_course = course.get_course_by_id(good["good_id"])
                    if tmp_course.used + count > tmp_course.capacity:
                        transaction.savepoint_rollback(save_point)
                        return Response({
                            "good_id": good["good_id"],
                            "type": good["type"],
                            "error": "课程容量不足"
                        }, status=status.HTTP_400_BAD_REQUEST)
                    tmp_course.used += count
                    tmp_course.save()
                # 添加订单记录
                ref_serializer = OrderRefSerializer(data={
                    "good_id": good["good_id"],
                    "type": good["type"],
                    "org_id": params["org_id"],
                    "order_id": order_serializer.data["id"],
                    "price": tmp_course.price
                })
                if ref_serializer.is_valid():
                    ref_serializer.save()
                    # 从购物车中移除
                    shopping_cart_item = shopping.get_shopping_cart(good["good_id"], params["user_id"],
                                                                    good["type"], params["org_id"])
                    shopping_cart_item.status = 0
                    shopping_cart_item.save()
                else:
                    transaction.savepoint_rollback(save_point)
                    return Response({
                        "good_id": good["good_id"],
                        "type": good["type"],
                        "error": "无法添加课程"
                    }, status=status.HTTP_400_BAD_REQUEST)
                # 登记下用户购买的课程、价格及数量
                user_ref_serializer = CourseUserRefSerializer(data={
                    "good_id": good["good_id"],
                    "user_id": params["user_id"],
                    "type": good["type"],
                    "count": count,
                    "price": good["price"],
                    "org_id": params["org_id"]
                })
                if user_ref_serializer.is_valid():
                    user_ref_serializer.save()
                else:
                    return Response({
                        "error": "无法添加课程"
                    }, status=status.HTTP_400_BAD_REQUEST)
            transaction.savepoint_commit(save_point)
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)


class OrderList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        user_id = None
        if 'user_id' in params:
            user_id = params['user_id']
        offset, limit = 1, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None

        order_list = order.list_order(user_id=user_id, org_id=org_id, offset=offset, limit=limit)

        if user_id is not None:
            data_list = []
            user_info = people.get_user_by_id(user_id)
            for o in order_list:
                order_id, user_id, pay_time = o.id, o.user_id, o.pay_time
                order_refs = order.get_order_ref_by_order_id(order_id)
                course_ids = []
                for refs in order_refs:
                    if refs.type == OrderRef.Type.COURSE.value:
                        course_ids.append(refs.good_id)
                courses = course.list_course_by_id(course_ids)
                course_infos = []
                for c in courses:
                    course_infos.append({
                        "name": c.name,
                        "price": c.price,
                        "used": c.used,
                        "capacity": c.capacity,
                        "start_time": c.start_time,
                        "end_time": c.end_time
                    })
                data_list.append({
                    "id": o.id,
                    "username": user_info.username,
                    "phone": user_info.phone,
                    "email": user_info.email,
                    "gender": user_info.gender,
                    "course": course_infos
                })
            return Response({
                "list": data_list,
                "total": order.count_order(user_id, org_id)
            }, status=status.HTTP_200_OK)
        else:
            data_list = []
            for o in order_list:
                user_info = people.get_user_by_id(o.user_id)
                data_list.append({
                    "id": o.id,
                    "user_id": o.user_id,
                    "pay_time": o.pay_time,
                    "username": user_info.username,
                    "phone": user_info.phone,
                    "email": user_info.email,
                    "gender": user_info.gender
                })
            return Response({
                "list": data_list,
                "total": order.count_order(user_id, org_id)
            }, status=status.HTTP_200_OK)
