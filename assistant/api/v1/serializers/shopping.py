from assistant.models import ShoppingCart
from rest_framework import serializers


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'org_id', 'status',
                  'user_id', 'good_id', 'type']
