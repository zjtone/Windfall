from assistant.models import Org
from rest_framework import serializers


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ['id', 'org_id', 'status',
                  'name', 'description', 'email', 'password']
