from assistant.models import Order, OrderRef


def get_order(order_id):
    return Order.objects.filter(id=order_id).get()


def get_order_ref_by_order_id(order_id):
    return OrderRef.objects.filter(order_id=order_id).all()


def list_order_ref_by_order_ids(ids):
    return OrderRef.objects.filter(order_id__in=ids).all()


def list_order(user_id, org_id, offset=0, limit=10):
    orders = Order.objects.filter(org_id=org_id, status=1)
    if user_id is not None:
        orders = orders.filter(user_id=user_id)
    return orders.all()[(offset-1) * limit:offset * limit]


def count_order(user_id, org_id):
    orders = Order.objects.filter(org_id=org_id, status=1)
    if user_id is not None:
        orders = orders.filter(user_id=user_id)
    return orders.count()
