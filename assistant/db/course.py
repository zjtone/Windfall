from assistant.models import Course


def course2dict(course):
    return {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "img": course.img,
        "status": course.status
    }


def course_list2dict(courses):
    return {
        "data": [course2dict(c) for c in courses]
    }


def create_course(name, description, img, org_id):
    course = Course(name=name, description=description,
                    img=img, org_id=org_id)
    course.save()
    return course


def get_course_by_id(_id):
    course = Course.objects.filter(id=_id).get()
    return course2dict(course)


def get_course_list(offset, limit):
    course_list = Course.objects.filter(status=1).all()
    return course_list2dict(course_list[offset:limit])
