from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from assistant.api.v1.serializers.auth_user import AuthUserSerializer, AuthUserRefSerializer
from assistant.api.apiviews import MyAPIView
from assistant.models import AuthUserRef
from django.contrib.auth.hashers import make_password


class AuthUserApi(MyAPIView):
    # 身份验证和权限是两个概念，只设定权限仍然会进行身份验证，需要设定不需要身份验证
    permission_classes = [AllowAny]  # 权限
    authentication_classes = []  # 身份验证

    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ref_serializer = AuthUserRefSerializer(data={
                "auth_id": serializer.data["id"],
                "type": request.data.get("type", AuthUserRef.Type.INVALID.value),
                "org_id": request.data.get("org_id", -1)
            })
            if ref_serializer.is_valid():
                ref_serializer.save()
                return Response("success", status=status.HTTP_201_CREATED)
            else:
                return Response(ref_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
