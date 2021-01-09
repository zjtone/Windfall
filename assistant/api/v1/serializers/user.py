from assistant.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'org_id', 'status',
                  'username', 'password', 'id_card',
                  'phone', 'email', 'openid', 'leader_id']
