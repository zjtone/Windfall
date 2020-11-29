import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from assistant.models import Emploee
from assistant.db.people import get_employee_by_id, create_employee


def get_employee(request):
    params = request.GET
    _id = params["id"]
    try:
        return JsonResponse(get_employee_by_id(_id))
    except Emploee.DoesNotExist as e:
        return HttpResponse(status=404)


def post_employee(request):
    data = json.loads(request.body.decode("utf-8"))
    employee = create_employee(username=data.get("username", ""), password=data.get("password", ""),
                               id_card=data.get("id_card", ""), phone=data.get("phone", ""),
                               email=data.get("email", ""), openid=data.get("openid", ""),
                               leader_id=data.get("leader_id", ""), org_id=data.get("org_id", ""))
    return HttpResponse(str(employee.id))


def put_employee(request):
    return HttpResponse("put")


def delete_employee(request):
    return HttpResponse("delete")


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index(request):
    if request.method == "GET":
        return get_employee(request)
    elif request.method == "POST":
        return post_employee(request)
    elif request.method == "PUT":
        return put_employee(request)
    elif request.method == "DELETE":
        return delete_employee(request)
    return HttpResponse(status=405, content="not allowed")
