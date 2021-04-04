from assistant.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'org_id', 'status', 'img',
                  'username', 'id_card', 'description',
                  'phone', 'email', 'openid', 'leader_id']
