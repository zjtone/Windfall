from assistant.models import Employee, Teacher, User, AuthUserRef
from assistant.db.base import get_by_id


def get_employee_by_id(_id):
    return get_by_id(Employee, _id)


def get_teacher_by_id(_id):
    return get_by_id(Teacher, _id)


def get_user_by_id(_id):
    return get_by_id(User, _id)


def get_people_by_auth_id(auth_id):
    return AuthUserRef.objects.filter(auth_id=auth_id).get()


def list_employee(org_id, offset, limit):
    return Employee.objects.filter(org_id=org_id) \
               .filter(id__gt=max((offset - 1) * limit + 1, 0)).all()[:limit]


def count_employee(org_id, status=1):
    return Employee.objects.filter(org_id=org_id, status=status).count()


def list_teacher(org_id, offset, limit):
    return Teacher.objects.filter(org_id=org_id) \
               .filter(id__gt=max((offset - 1) * limit + 1, 0)).all()[:limit]


def count_teacher(org_id, status=1):
    return Teacher.objects.filter(org_id=org_id, status=status).count()


def list_user(org_id, offset, limit):
    return User.objects.filter(org_id=org_id) \
               .filter(id__gt=max((offset - 1) * limit + 1, 0)).all()[:limit]


def count_user(org_id, status=1):
    return User.objects.filter(org_id=org_id, status=status).count()
