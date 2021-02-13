from assistant.models import Employee, Teacher, User, AuthUserRef
from assistant.db.base import get_by_id


def get_employee_by_id(_id):
    return get_by_id(Employee, _id)


def get_teacher_by_id(_id):
    return get_by_id(Teacher, _id)


def get_user_by_id(_id):
    return get_by_id(User, _id)


def list_employee_by_id(ids, status=1):
    return Employee.objects.filter(id__in=ids, status=status).all()


def list_teacher_by_id(ids, status=1):
    return Teacher.objects.filter(id__in=ids, status=status).all()


def list_user_by_id(ids, status=1):
    return User.objects.filter(id__in=ids, status=status).all()


def get_people_by_auth_id(auth_id):
    return AuthUserRef.objects.filter(auth_id=auth_id).get()


def list_employee(org_id, offset, limit, status=None):
    data_list = Employee.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.all()[(offset-1) * limit:offset * limit]


def count_employee(org_id, status=1):
    data_list = Employee.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.count()


def list_teacher(org_id, offset, limit, status=None):
    data_list = Teacher.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.all()[(offset-1) * limit:offset * limit]


def count_teacher(org_id, status=1):
    data_list = Teacher.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.count()


def list_user(org_id, offset, limit, status=None):
    data_list = User.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.all()[(offset-1) * limit:offset * limit]


def count_user(org_id, status=1):
    data_list = User.objects.filter(org_id=org_id)
    if status:
        data_list = data_list.filter(status=status)
    return data_list.count()
