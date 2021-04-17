import json
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.course import CourseSerializer
from assistant.api.v1.serializers.order import OrderSerializer, OrderRefSerializer
from assistant.db import course, people, order
from assistant.api.apiviews import MyAPIView
from django.http import HttpResponse


class OrderApi(MyAPIView):
    def get(self, request):
        params = request.data
        if 'order_id' not in params or 'org_id' not in params:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        user_order = order.get_order(params["order_id"])
        order_list = order.get_order_ref_by_order_id(params["order_id"])
        course_ids = []
        for good in order_list:
            if good["type"] == 0:
                # 课程
                course_ids.append(good["good_id"])
        return Response({
            "courses": CourseSerializer(course.list_course_by_id(course_ids), many=True).data
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
                {"good_id": 1, "type": 1},
                {"good_id": 2, "type": 0}
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
                if good["type"] == 0:
                    tmp_course = course.get_course_by_id(good["good_id"])
                    if tmp_course.used >= tmp_course.capacity:
                        transaction.savepoint_rollback(save_point)
                        return Response({
                            "good_id": good["good_id"],
                            "type": good["type"],
                            "error": "课程容量不足"
                        }, status=status.HTTP_400_BAD_REQUEST)
                    tmp_course.used += 1
                    tmp_course.save()
                ref_serializer = OrderRefSerializer(data={"good_id": good["good_id"], \
                    "type": good["type"], "org_id": params["org_id"]})
                if ref_serializer.is_valid():
                    ref_serializer.save()
                else:
                    transaction.savepoint_rollback(save_point)
                    return Response({
                        "good_id": good["good_id"],
                        "type": good["type"],
                        "error": ref_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            transaction.savepoint_commit(save_point)
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)


class OrderList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params and 'user_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        user_id = params['user_id']
        offset, limit = 0, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None
        return Response({
            "data": OrderSerializer(
                order.list_order(user_id=user_id, org_id=org_id, offset=offset, limit=limit), 
                many=True).data
        }, status=status.HTTP_200_OK)
