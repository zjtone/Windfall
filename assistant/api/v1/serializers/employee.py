from assistant.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'org_id', 'status', 'img',
                  'username', 'password', 'id_card',
                  'phone', 'email', 'openid', 'leader_id']
