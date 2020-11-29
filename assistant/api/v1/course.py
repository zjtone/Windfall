import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from assistant.models import Course
from assistant.db.course import get_course_by_id, create_course
# from assistant.utils import require_GET, require_POST, require_PUT, require_DELETE


def get_course(request):
    params = request.GET
    _id = params["id"]
    try:
        return JsonResponse(get_course_by_id(_id))
    except Course.DoesNotExist as e:
        return HttpResponse(status=404)


def post_course(request):
    data = json.loads(request.body.decode("utf-8"))
    course = create_course(name=data.get("name", ""), description=data.get("description", ""),
                           img=data.get("img", ""), org_id=data.get("org_id", ""))
    return HttpResponse(str(course.id))


def put_course(request):
    return HttpResponse("put")


def delete_course(request):
    return HttpResponse("delete")


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index(request):
    if request.method == "GET":
        return get_course(request)
    elif request.method == "POST":
        return post_course(request)
    elif request.method == "PUT":
        return put_course(request)
    elif request.method == "DELETE":
        return delete_course(request)
    return HttpResponse(status=405, content="not allowed")
