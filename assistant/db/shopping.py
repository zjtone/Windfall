from assistant.models import ShoppingCart
from assistant.db.course import list_course_by_id


def get_shopping_cart(user_id, org_id, offset=0, limit=10):
    shopping_carts = ShoppingCart.objects.filter(org_id=org_id, user_id=user_id,
                                                 id__gt=offset, status=1).all()[:limit]
    course_ids = [sc.course_id for sc in shopping_carts]
    return list_course_by_id(course_ids)


def list_shopping_cart(org_id, offset, limit):
    return ShoppingCart.objects.filter(org_id=org_id) \
               .filter(id__gt=max((offset - 1) * limit + 1, 0)).all()[:limit]


def count_shopping_cart(org_id, status=1):
    return ShoppingCart.objects.filter(org_id=org_id, status=status).count()
