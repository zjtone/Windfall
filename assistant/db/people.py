from assistant.models import Emploee, Teacher


def create_people(model, username, password, id_card,
                  phone, email, openid, org_id, leader_id=-1):
    people = model(name=username, password=password, id_card=id_card, phone=phone,
                   email=email, openid=openid, org_id=org_id, leader_id=leader_id)
    people.save()


def create_employee(username, password, id_card,
                    phone, email, openid, org_id, leader_id=-1):
    return create_people(Emploee, username, password, id_card, phone, email, openid, org_id, leader_id=leader_id)


def create_teacher(username, password, id_card,
                   phone, email, openid, org_id, leader_id=-1):
    return create_people(Teacher, username, password, id_card, phone, email, openid, org_id, leader_id=leader_id)


def get_people_by_id(model, _id):
    people = model.objects.filter(id=_id).get()
    return {
        "username": people.username,
        "password": people.password,
        "id_card": people.id_card,
        "phone": people.phone,
        "email": people.email,
        "openid": people.openid,
        "leader_id": people.leader_id
    }


def get_employee_by_id(_id):
    return get_people_by_id(Emploee, _id)


def get_teacher_by_id(_id):
    return get_people_by_id(Teacher, _id)
