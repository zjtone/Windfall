from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef, CourseTimeRef, Time, CourseUserRef
from assistant.api.v1.serializers.course import CourseTagSerializer


def get_course_by_id(_id):
    return Course.objects.filter(id=_id).get()


def list_course_by_id(ids):
    return Course.objects.filter(id__in=ids, status=1).all()


def get_tag_by_id(_id):
    return Tag.objects.filter(id=_id).get()


def list_tag_by_id(ids, status=1):
    return Tag.objects.filter(id__in=ids, status=status).all()


def list_time_by_id(ids, status=1):
    return Time.objects.filter(id__in=ids, status=status).all()


def get_tag_ref_by_course_id(course_id, status=1):
    return CourseTagRef.objects.filter(course_id=course_id, status=status).all()


def get_teacher_ref_by_course_id(course_id, status=1):
    return CourseTeacherRef.objects.filter(course_id=course_id, status=status).all()


def get_time_ref_by_course_id(course_id, status=1):
    return CourseTimeRef.objects.filter(course_id=course_id, status=status).all()


def list_course(org_id, offset, limit, status=None):
    course_list = Course.objects.filter(org_id=org_id)
    if status:
        course_list = course_list.filter(status=status)
    return course_list.all()[(offset-1) * limit:offset * limit]


def count_course(org_id, status=1):
    course_list = Course.objects.filter(org_id=org_id)
    if status:
        course_list = course_list.filter(status=status)
    return course_list.count()


def list_course_with_user(user_id, offset, limit, status=None):
    refs = CourseUserRef.objects.filter(user_id=user_id)
    if status:
        refs = refs.filter(status=status)
    refs = refs.all()[(offset-1) * limit:offset * limit]
    return list_course_by_id([ref["course_id"] for ref in refs])


def count_course_with_user(user_id, status=None):
    refs = CourseUserRef.objects.filter(user_id=user_id)
    if status:
        refs = refs.filter(status=status)
    return refs.count()


def list_course_with_teacher(teacher_id, offset, limit, status=None):
    refs = CourseTeacherRef.objects.filter(teacher_id=teacher_id)
    if status:
        refs = refs.filter(status=status)
    refs = refs.all()[(offset-1) * limit:offset * limit]
    return list_course_by_id([ref["course_id"] for ref in refs])


def count_course_with_teacher(teacher_id, status=None):
    refs = CourseTeacherRef.objects.filter(teacher_id=teacher_id)
    if status:
        refs = refs.filter(status=status)
    return refs.count()


def list_tag(org_id, status=1):
    tag_list = Tag.objects.filter(org_id=org_id)
    if status:
        tag_list = tag_list.filter(status=status)
    return tag_list.all()


def get_course_tag_ref(course_id, tag_id, status=1):
    try:
        return CourseTagRef.objects.filter(course_id=course_id, tag_id=tag_id, status=status).get()
    except:
        return None


def course_tags(course_id, tag_ids, org_id):
    # 'id', 'org_id', 'status', 'course_id', 'tag_id'
    course_tag_list = get_tag_ref_by_course_id(course_id)
    old_ids = {c_tag["tag_id"] for c_tag in course_tag_list}
    # create
    for tag_id in set(tag_ids) - old_ids:
        serializer = CourseTagSerializer(data={
            "org_id": org_id,
            "course_id": course_id,
            "tag_id": tag_id
        })
        if serializer.is_valid():
            serializer.save()
        else:
            raise Exception(str(serializer.errors))
    # delete
    for tag_id in old_ids - set(tag_ids):
        old_course_tag = get_course_tag_ref(course_id, tag_id)
        old_course_tag.status = 0
        old_course_tag.save()


def get_course_teacher_ref(course_id, teacher_id, status=1):
    try:
        return CourseTeacherRef.objects.filter(course_id=course_id, teacher_id=teacher_id, status=status).get()
    except:
        return None


def course_teachers(course_id, teacher_ids, org_id):
    # 'id', 'org_id', 'status', 'course_id', 'teacher_id'
    course_teacher_list = get_teacher_ref_by_course_id(course_id)
    old_ids = {c_teacher["teacher_id"] for c_teacher in course_teacher_list}
    # create
    for teacher_id in set(teacher_ids) - old_ids:
        serializer = CourseTagSerializer(data={
            "org_id": org_id,
            "course_id": course_id,
            "teacher_id": teacher_id
        })
        if serializer.is_valid():
            serializer.save()
        else:
            raise Exception(str(serializer.errors))
    # delete
    for teacher_id in old_ids - set(teacher_ids):
        old_course_teacher = get_course_teacher_ref(course_id, teacher_id)
        old_course_teacher.status = 0
        old_course_teacher.save()


def get_course_time_ref(course_id, time_id, status=1):
    try:
        return CourseTeacherRef.objects.filter(course_id=course_id, time_id=time_id, status=status).get()
    except:
        return None


def course_times(course_id, time_ids, org_id):
    # 'id', 'org_id', 'status', 'course_id', 'time_id'
    course_time_list = get_time_ref_by_course_id(course_id)
    old_ids = {c_time["time_id"] for c_time in course_time_list}
    # create
    for time_id in set(time_ids) - old_ids:
        serializer = CourseTagSerializer(data={
            "org_id": org_id,
            "course_id": course_id,
            "time_id": time_id
        })
        if serializer.is_valid():
            serializer.save()
        else:
            raise Exception(str(serializer.errors))
    # delete
    for time_id in old_ids - set(time_ids):
        old_course_time = get_course_time_ref(course_id, time_id)
        old_course_time.status = 0
        old_course_time.save()
