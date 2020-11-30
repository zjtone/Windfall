import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from assistant.models import User
from assistant.db.people import get_user_by_id, create_user


def get_user(request):
    params = request.GET
    _id = params["id"]
    try:
        return JsonResponse(get_user_by_id(_id))
    except User.DoesNotExist as e:
        return HttpResponse(status=404)


def post_user(request):
    data = json.loads(request.body.decode("utf-8"))
    user = create_user(username=data.get("username", ""), password=data.get("password", ""),
                       id_card=data.get("id_card", ""), phone=data.get("phone", ""),
                       email=data.get("email", ""), openid=data.get("openid", ""),
                       leader_id=int(data.get("leader_id", "0")), org_id=int(data.get("org_id", "0")))
    return HttpResponse(str(user.id))


def put_user(request):
    return HttpResponse("put")


def delete_user(request):
    return HttpResponse("delete")


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index(request):
    if request.method == "GET":
        return get_user(request)
    elif request.method == "POST":
        return post_user(request)
    elif request.method == "PUT":
        return put_user(request)
    elif request.method == "DELETE":
        return delete_user(request)
    return HttpResponse(status=405, content="not allowed")
