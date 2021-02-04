from assistant.models import Org
from rest_framework import serializers


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ['id', 'org_id', 'status', 'img',
                  'name', 'description', 'email', 'password']
