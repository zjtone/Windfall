from assistant.models import Emploee, Teacher, User
from assistant.db.base import get_by_id


def create_people(model, username, password, id_card,
                  phone, email, openid, org_id, leader_id=-1):
    people = model(username=username, password=password, id_card=id_card, phone=phone,
                   email=email, openid=openid, org_id=org_id, leader_id=leader_id)
    people.save()
    return people


def create_employee(username, password, id_card,
                    phone, email, openid, org_id, leader_id=-1):
    return create_people(Emploee, username, password, id_card, phone, email, openid, org_id, leader_id=leader_id)


def create_teacher(username, password, id_card,
                   phone, email, openid, org_id, leader_id=-1):
    return create_people(Teacher, username, password, id_card, phone, email, openid, org_id, leader_id=leader_id)


def create_user(username, password, id_card,
                phone, email, openid, org_id, leader_id=-1):
    return create_people(User, username, password, id_card, phone, email, openid, org_id, leader_id=leader_id)


def get_employee_by_id(_id):
    return get_by_id(Emploee, _id)


def get_teacher_by_id(_id):
    return get_by_id(Teacher, _id)


def get_user_by_id(_id):
    return get_by_id(User, _id)
