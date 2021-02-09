from assistant.models import Course, Tag


def get_course_by_id(_id):
    return Course.objects.filter(id=_id).get()


def list_course_by_id(ids):
    return Course.objects.filter(id__in=ids, status=1).all()


def get_tag_by_id(_id):
    return Tag.objects.filter(id=_id).get()


def list_course(org_id, offset, limit):
    return Course.objects.filter(org_id=org_id).all()[(offset-1) * limit:offset * limit]


def count_course(org_id, status=1):
    return Course.objects.filter(org_id=org_id, status=status).count()


def list_tag(org_id, status=1):
    return Tag.objects.filter(org_id=org_id, status=status).all()
