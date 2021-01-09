from assistant.models import Course


def get_course_by_id(_id):
    return Course.objects.filter(id=_id).get()

