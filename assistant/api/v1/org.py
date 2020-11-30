import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from assistant.models import Org
from assistant.db.org import get_org_by_id, create_org


def get_org(request):
    params = request.GET
    _id = params["id"]
    try:
        return JsonResponse(get_org_by_id(_id))
    except Org.DoesNotExist as e:
        return HttpResponse(status=404)


def post_org(request):
    data = json.loads(request.body.decode("utf-8"))
    org = create_org(name=data.get("name"), description=data.get("description"),
                     email=data.get("email"), password=data.get("password"))
    return HttpResponse(str(org.id))


def put_org(request):
    return HttpResponse("put")


def delete_org(request):
    return HttpResponse("delete")


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index(request):
    if request.method == "GET":
        return get_org(request)
    elif request.method == "POST":
        return post_org(request)
    elif request.method == "PUT":
        return put_org(request)
    elif request.method == "DELETE":
        return delete_org(request)
    return HttpResponse(status=405, content="not allowed")
