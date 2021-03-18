from assistant.models import Order, OrderRef
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'org_id', 'status', 'user_id']


class OrderRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRef
        fields = ['id', 'org_id', 'status', 
        'order_id', "good_id", "type"]
