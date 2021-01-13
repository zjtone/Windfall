from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef, Teacher


def get_course_by_id(_id):
    return Course.objects.filter(id=_id).get()


def get_tag_by_id(_id):
    return Tag.objects.filter(id=_id).get()


def course_to_tag(course_id, status=1):
    refs = CourseTagRef.objects.filter(course_id=course_id, status=status).all()
    if not refs:
        return None
    ref_ids = [ref.tag_id for ref in refs]
    return Tag.objects.filter(id__in=ref_ids).all()


def course_to_teacher(course_id, status=1):
    refs = CourseTeacherRef.objects.filter(course_id=course_id, status=status).all()
    if not refs:
        return None
    ref_ids = [ref.teacher_id for ref in refs]
    return Teacher.objects.filter(id__in=ref_ids).all()
