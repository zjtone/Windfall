from django.http import Http404
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from assistant.models import AuthUserRef
from assistant.api.v1.serializers.user import UserSerializer
from assistant.db import people, base, org
from assistant.api.apiviews import MyAPIView
from django.contrib.auth.hashers import make_password


def create_user(params):
    params['password'] = make_password(params['password'])

    if 'org_id' not in params:
        return Response("非法机构！", status=status.HTTP_400_BAD_REQUEST)
    org_id = params["org_id"]
    _org = org.get_org_by_id(org_id)
    if _org is None:
        return Response("非法机构！", status=status.HTTP_400_BAD_REQUEST)

    with transaction.atomic():
        save_point = transaction.savepoint()
        # 创建用户
        serializer = UserSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
        else:
            transaction.savepoint_rollback(save_point)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        result = base.create_auth_user(serializer.data['id'], params['username'], params['password'],
                                       params['org_id'], AuthUserRef.Type.USER.value)
        if result is None:
            transaction.savepoint_commit(save_point)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            transaction.savepoint_rollback(save_point)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class CreateUserApi(MyAPIView):
    permission_classes = [AllowAny]  # 权限
    authentication_classes = []  # 身份验证

    def post(self, request):
        params = request.data
        return create_user(params)


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
        params['password'] = make_password(params['password'])

        if "id" in params:
            return UserApi.update(request)

        return create_user(params)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if 'org_id' in params:
                return Response("非法！机构不能修改！", status=status.HTTP_400_BAD_REQUEST)
            if "id" in params:
                update_user = request.data
                exist_user = people.get_user_by_id(params["id"])
                for key in update_user:
                    if hasattr(exist_user, key):
                        setattr(exist_user, key, update_user[key])
                exist_user.save()

                # 修改密码
                if 'password' in params:
                    password = make_password(params['password'])
                    if password != exist_user.password:
                        auth_user_ref = people.get_people_by_auth_id(auth_id=params['id'])
                        auth_user = people.get_auth_user_by_id(auth_user_ref.id)
                        auth_user.password = password
                        auth_user.save()

                return Response("", status=status.HTTP_200_OK)
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)


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
