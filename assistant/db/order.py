from assistant.models import Order, OrderRef


def get_order(order_id):
    return Order.objects.filter(id=order_id).get()


def get_order_ref_by_order_id(order_id):
    return OrderRef.objects.filter(order_id=order_id).all()


def list_order(user_id, org_id, offset=0, limit=10):
    orders = Order.objects.filter(org_id=org_id, user_id=user_id, status=1)\
        .all()[(offset-1) * limit:offset * limit]
    return orders
