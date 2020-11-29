from assistant.models import Course


def create_course(name, description, img, org_id):
    course = Course(name=name, description=description,
                    img=img, org_id=org_id)
    course.save()
    return course


def get_course_by_id(_id):
    course = Course.objects.filter(id=_id).get()
    return {
        "name": course.name,
        "description": course.description,
        "img": course.img
    }

