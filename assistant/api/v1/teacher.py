import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from assistant.models import Teacher
from assistant.db.people import get_teacher_by_id, create_teacher


def get_teacher(request):
    params = request.GET
    _id = params["id"]
    try:
        return JsonResponse(get_teacher_by_id(_id))
    except Teacher.DoesNotExist as e:
        return HttpResponse(status=404)


def post_teacher(request):
    data = json.loads(request.body.decode("utf-8"))
    teacher = create_teacher(username=data.get("username", ""), password=data.get("password", ""),
                             id_card=data.get("id_card", ""), phone=data.get("phone", ""),
                             email=data.get("email", ""), openid=data.get("openid", ""),
                             leader_id=int(data.get("leader_id", "0")), org_id=int(data.get("org_id", "0")))
    return HttpResponse(str(teacher.id))


def put_teacher(request):
    return HttpResponse("put")


def delete_teacher(request):
    return HttpResponse("delete")


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index(request):
    if request.method == "GET":
        return get_teacher(request)
    elif request.method == "POST":
        return post_teacher(request)
    elif request.method == "PUT":
        return put_teacher(request)
    elif request.method == "DELETE":
        return delete_teacher(request)
    return HttpResponse(status=405, content="not allowed")
