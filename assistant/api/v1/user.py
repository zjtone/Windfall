from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.user import UserSerializer
from assistant.db import people
from assistant.api.apiviews import MyAPIView


class UserApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                user = people.get_user_by_id(_id)
                return Response(UserSerializer(user).data)
            raise Http404
        except Exception as e:
            print('[UserApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        params = request.data
        if "id" in params:
            return UserApi.update(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if "id" in params:
                update_user = request.data
                exist_user = people.get_user_by_id(params["id"])
                for key in update_user:
                    if hasattr(exist_user, key):
                        setattr(exist_user, key, update_user[key])
                exist_user.save()
                return Response("", status=status.HTTP_200_OK)
            raise Http404
        except Exception as e:
            raise Http404


class UserList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        offset, limit = 1, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None
        # 返回课程对应的用户列表
        if 'course_id' in params:
            return Response({
                "data": UserSerializer(
                    people.list_user_with_course(params["course_id"], offset, limit, data_status), many=True).data,
                "total": people.count_user_with_course(params["course_id"], data_status)
            })
        # 没有过滤条件，返回用户列表
        return Response({
            "data": UserSerializer(people.list_user(org_id, offset, limit, data_status), many=True).data,
            "total": people.count_user(org_id, data_status)
        }, status=status.HTTP_200_OK)
