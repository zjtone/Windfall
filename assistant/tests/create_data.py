import json
import random
from urllib import request


base_url = "http://localhost:8000/api/"
start, end = 0, 100


def create_organization():
    url = base_url + "organization/"
    for i in range(start, end):
        data = json.dumps({
            "name": "name_{}".format(i),
            "description": "description_{}".format(i),
            "email": "email_{}@mail.com".format(i),
            "password": "password"
        })
        req = request.Request(url=url, data=data.encode("utf-8"), method='POST', headers={"Content-Type": "application/json"})
        with request.urlopen(req) as f:
            print(f.status)
            print(f.reason)


def create_course():
    url = base_url + "course/"
    for i in range(start, end):
        data = json.dumps({
            "name": "name_{}".format(i),
            "description": "description_{}".format(i),
            "img": "email_{}@mail.com".format(i),
            "org_id": random.randint(start, end)
        })
        req = request.Request(url=url, data=data.encode("utf-8"), method='POST', headers={"Content-Type": "application/json"})
        with request.urlopen(req) as f:
            print(f.status)
            print(f.reason)


def create_employee():
    url = base_url + "employee/"
    for i in range(start, end):
        data = json.dumps({
            "username": "username_{}".format(i),
            "password": "password_{}".format(i),
            "id_card": str(random.randint(1, 100000)),
            "openid": str(random.randint(1, 100000)),
            "phone": "phone_{}@mail.com".format(i),
            "email": "email_{}@mail.com".format(i),
            "org_id": random.randint(start, end)
        })
        req = request.Request(url=url, data=data.encode("utf-8"), method='POST', headers={"Content-Type": "application/json"})
        with request.urlopen(req) as f:
            print(f.status)
            print(f.reason)


def create_teacher():
    url = base_url + "teacher/"
    for i in range(start, end):
        data = json.dumps({
            "username": "username_{}".format(i),
            "password": "password_{}".format(i),
            "id_card": str(random.randint(1, 100000)),
            "openid": str(random.randint(1, 100000)),
            "phone": "phone_{}@mail.com".format(i),
            "email": "email_{}@mail.com".format(i),
            "org_id": random.randint(start, end)
        })
        req = request.Request(url=url, data=data.encode("utf-8"), method='POST', headers={"Content-Type": "application/json"})
        with request.urlopen(req) as f:
            print(f.status)
            print(f.reason)


def create_user():
    url = base_url + "user/"
    for i in range(start, end):
        data = json.dumps({
            "username": "username_{}".format(i),
            "password": "password_{}".format(i),
            "id_card": str(random.randint(1, 100000)),
            "openid": str(random.randint(1, 100000)),
            "phone": "phone_{}@mail.com".format(i),
            "email": "email_{}@mail.com".format(i),
            "org_id": random.randint(start, end)
        })
        req = request.Request(url=url, data=data.encode("utf-8"), method='POST', headers={"Content-Type": "application/json"})
        with request.urlopen(req) as f:
            print(f.status)
            print(f.reason)


if __name__ == '__main__':
    # create_organization()
    # create_course()
    # create_employee()
    # create_teacher()
    create_user()
