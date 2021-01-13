from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef, Teacher


def get_course_by_id(_id):
    return Course.objects.filter(id=_id).get()


def get_tag_by_id(_id):
    return Tag.objects.filter(id=_id).get()
