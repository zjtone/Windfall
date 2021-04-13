import json
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.course import CourseSerializer
from assistant.api.v1.serializers.shopping import ShoppingCartSerializer
from assistant.db import shopping, course, people
from assistant.api.apiviews import MyAPIView
from django.http import HttpResponse


class ShoppingCartApi(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        offset, limit = 0, 10
        if 'offset' in params:
            offset = int(params['offset'])
        if 'limit' in params:
            limit = min(int(params['limit']), 50)
        # 返回用户购物车中的所有课程
        if 'user_id' in params:
            return Response({
                "data": CourseSerializer(
                    shopping.list_shopping_cart_course_with_user(
                        user_id=params['user_id'], org_id=params['org_id'], 
                        offset=offset, limit=limit), many=True).data,
                "total": shopping.count_shopping_cart_course_with_user(
                    user_id=params['user_id'], org_id=params['org_id'])
            }, status=status.HTTP_200_OK)
        # 返回添加了课程的所有用户
        if "course_id" in params:
            return Response({
                "data": CourseSerializer(
                    shopping.list_shopping_cart_user_with_course(course_id=params['course_id'], org_id=params['org_id'],
                        offset=offset, limit=limit), many=True).data,
                "total": shopping.count_shopping_cart_user_with_course(
                    course_id=params['course_id'], org_id=params['org_id'])
            }, status=status.HTTP_200_OK)
        return Response("invalid", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        params = request.data
        if "id" in params:
            return ShoppingCartApi.update(request)
        if shopping.get_shopping_cart(params['good_id'], params['user_id'],
                                      params['type'], params['org_id']) is not None:
            return Response('exists', status=status.HTTP_200_OK)
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if "id" in params:
                update_shopping_cart = request.data
                exist_shopping_cart = shopping.get_shopping_cart_by_id(params["id"])
                for key in update_shopping_cart:
                    if hasattr(exist_shopping_cart, key):
                        setattr(exist_shopping_cart, key, update_shopping_cart[key])
                exist_shopping_cart.save()
                return Response("", status=status.HTTP_200_OK)
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)


class ShoppingCartList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        offset, limit = 0, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None
        user_id = None
        if 'user_id' in params:
            user_id = params['user_id']

        shopping_list = shopping.list_shopping_cart(org_id, user_id, offset, limit, data_status)
        user_ids, course_ids = set(), set()
        for shopping_cart in shopping_list:
            user_ids.add(shopping_cart.user_id)
            course_ids.add(shopping_cart.good_id)
        user_list = people.list_auth_user_by_id(user_ids)
        course_list = course.list_course_by_id(course_ids)
        
        user_dict, course_dict = {}, {}
        for tmp_user in user_list:
            user_dict[tmp_user.id] = tmp_user
        for tmp_course in course_list:
            course_dict[tmp_course.id] = tmp_course
        
        result_list = []
        for shopping_cart in shopping_list:
            tmp_user = user_dict[shopping_cart.user_id]
            tmp_course = course_dict[shopping_cart.good_id]
            if tmp_user and tmp_course:
                result_list.append({
                    "id": shopping_cart.id,
                    "user_id": tmp_user.id,
                    "username": tmp_user.username,
                    "phone": tmp_user.phone,
                    "email": tmp_user.email,
                    "user_status": tmp_user.status,
                    "good_id": tmp_course.id,
                    "goodname": tmp_course.name,
                    "good_status": tmp_course.status,
                    "status": shopping_cart.status,
                    "org_id": shopping_cart.org_id
                })
        return HttpResponse(json.dumps({
            "data": result_list,
            "total": shopping.count_shopping_cart(org_id, user_id, data_status)
        }))
