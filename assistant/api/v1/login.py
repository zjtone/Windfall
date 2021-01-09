from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.auth_user import AuthUserSerializer
from django.contrib.auth.hashers import make_password


class AuthUserApi(APIView):

    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        print(request.data)
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
