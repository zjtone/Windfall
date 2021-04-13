from assistant.models import AuthUserRef
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class AuthUserRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserRef
        fields = ['id', 'status', 'create_time', 'modify_time', 'delete_time',
                  'auth_id', 'type', 'org_id', 'auth_user_id']
