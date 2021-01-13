from assistant.models import ShoppingCart
from assistant.db.course import list_course_by_id


def get_shopping_cart(user_id, org_id, offset=0, limit=10):
    shopping_carts = ShoppingCart.objects.filter(org_id=org_id, user_id=user_id,
                                                 id__gt=offset, status=1).all()[:limit]
    course_ids = [sc.course_id for sc in shopping_carts]
    return list_course_by_id(course_ids)
