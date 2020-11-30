from assistant.models import Org


def create_org(name, description, email, password):
    org = Org(name=name, description=description,
              email=email, password=password, org_id=0)
    org.save()
    return org


def get_org_by_id(_id):
    org = Org.objects.filter(id=_id).get()
    return {
        "id": org.id,
        "name": org.name,
        "description": org.description,
        "email": org.email,
        "password": org.password
    }
