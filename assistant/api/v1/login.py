from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from assistant.api.v1.serializers.auth_user import AuthUserSerializer, AuthUserRefSerializer
from assistant.api.apiviews import MyAPIView
from django.contrib.auth.hashers import make_password


class AuthUserApi(MyAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ref_serializer = AuthUserRefSerializer(data={
                "auth_id": serializer.data["id"],
                "type": request.data["type"],
                "org_id": request.data["org_id"]
            })
            if ref_serializer.is_valid():
                ref_serializer.save()
                return Response("success", status=status.HTTP_201_CREATED)
            else:
                return Response(ref_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
