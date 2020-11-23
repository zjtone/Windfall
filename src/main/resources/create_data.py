import json
from urllib import request


base_url = "http://localhost:8080/"
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


if __name__ == '__main__':
    create_organization()
