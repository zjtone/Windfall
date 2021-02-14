from assistant.models import ShoppingCart
from assistant.db.course import list_course_by_id
from assistant.db.people import list_user_by_id


def get_shopping_cart_by_id(_id):
    return ShoppingCart.objects.filter(id=_id).get()


def list_shopping_cart_course_with_user(user_id, org_id, offset=0, limit=10):
    shopping_carts = ShoppingCart.objects.filter(
        org_id=org_id, user_id=user_id, 
        type=ShoppingCart.Type.COURSE.value, status=1).all()[(offset-1) * limit:offset * limit]
    course_ids = [sc['course_id'] for sc in shopping_carts]
    return list_course_by_id(course_ids)


def count_shopping_cart_course_with_user(user_id, org_id):
    shopping_carts = ShoppingCart.objects.filter(
        org_id=org_id, user_id=user_id, 
        type=ShoppingCart.Type.COURSE.value, status=1)
    return shopping_carts.count()


def list_shopping_cart_user_with_course(course_id, org_id, offset=0, limit=10):
    shopping_carts = ShoppingCart.objects.filter(
        org_id=org_id, good_id=course_id, 
        type=ShoppingCart.Type.COURSE.value, status=1).all()[(offset-1) * limit:offset * limit]
    user_ids = [sc['user_id'] for sc in shopping_carts]
    return list_user_by_id(user_ids)


def list_shopping_cart_user_with_course(course_id, org_id):
    shopping_carts = ShoppingCart.objects.filter(
        org_id=org_id, good_id=course_id, 
        type=ShoppingCart.Type.COURSE.value, status=1)
    return shopping_carts.count()


def list_shopping_cart(org_id, offset, limit, status=1):
    data_list = ShoppingCart.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.all()[(offset-1) * limit:offset * limit]


def count_shopping_cart(org_id, status=1):
    data_list = ShoppingCart.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.count()
