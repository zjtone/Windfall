from assistant.models import Org


def get_org_by_id(_id):
    return Org.objects.filter(id=_id).get()
