from django.http import Http404
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from assistant.models import AuthUserRef
from assistant.api.v1.serializers.org import OrgSerializer
from assistant.api.v1.serializers.auth_user import AuthUserSerializer, AuthUserRefSerializer
from assistant.db.org import get_org_by_id
from assistant.api.apiviews import MyAPIView
from django.contrib.auth.hashers import make_password


class OrgApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                org = get_org_by_id(_id)
                return Response(OrgSerializer(org).data)
            raise Http404
        except Exception as e:
            print('[OrgApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        params = request.data
        if "id" in params:
            return OrgApi.update(request)
        return Response("invalid", status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if "id" in params:
                update_org = request.data
                exist_org = get_org_by_id(params["id"])
                for key in update_org:
                    if hasattr(exist_org, key):
                        setattr(exist_org, key, update_org[key])
                exist_org.save()
                return Response("", status=status.HTTP_200_OK)
            raise Http404
        except Exception as e:
            raise Http404


class CreateOrg(MyAPIView):
    permission_classes = [AllowAny]  # 权限
    authentication_classes = []  # 身份验证

    def post(self, request):
        params = request.data
        params['password'] = make_password(params['password'])
        with transaction.atomic():
            save_point = transaction.savepoint()
            # 创建机构
            if "id" in params:
                return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
            serializer = OrgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                transaction.savepoint_rollback(save_point)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # 创建机构账号
            auth_user_serializer = AuthUserSerializer(data={
                'username': params['name'],
                'password': params['password']
            })
            if auth_user_serializer.is_valid():
                auth_user_serializer.save()
            else:
                transaction.savepoint_rollback(save_point)
                return Response(auth_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # 机构账号与用户账号关联
            auth_user_ref_serializer = AuthUserRefSerializer(data={
                'auth_id': auth_user_serializer.data['id'],
                'type': AuthUserRef.Type.ORG.value,
                'org_id': serializer.data['id']
            })
            if auth_user_ref_serializer.is_valid():
                auth_user_ref_serializer.save()
            else:
                transaction.savepoint_rollback(save_point)
                return Response(auth_user_ref_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            transaction.savepoint_commit(save_point)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)
