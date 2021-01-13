from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from assistant.api.v1.serializers.auth_user import AuthUserSerializer
from assistant.api.apiviews import MyAPIView
from django.contrib.auth.hashers import make_password


class AuthUserApi(MyAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
