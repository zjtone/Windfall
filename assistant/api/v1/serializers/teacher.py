from assistant.models import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'org_id', 'status', 'img',
                  'username', 'id_card',
                  'phone', 'email', 'openid', 'leader_id']
