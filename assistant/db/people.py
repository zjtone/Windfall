from assistant.models import Employee, Teacher, User
from assistant.db.base import get_by_id


def get_employee_by_id(_id):
    return get_by_id(Employee, _id)


def get_teacher_by_id(_id):
    return get_by_id(Teacher, _id)


def get_user_by_id(_id):
    return get_by_id(User, _id)
