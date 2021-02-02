from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.employee import EmployeeSerializer
from assistant.db import people
from assistant.api.apiviews import MyAPIView


class EmployeeApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                employee = people.get_employee_by_id(_id)
                return Response(EmployeeSerializer(employee).data)
            raise Http404
        except Exception as e:
            print('[EmployeeApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            params = request.data
            if "id" in params:
                update_employee = request.data
                exist_employee = people.get_employee_by_id(params["id"])
                for key in update_employee:
                    if hasattr(exist_employee, key):
                        setattr(exist_employee, key, update_employee[key])
                exist_employee.save()
                return Response("", status=status.HTTP_200_OK)
            raise Http404
        except Exception as e:
            raise Http404


class EmployeeList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        offset, limit = 0, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        return Response({
            "data": EmployeeSerializer(people.list_employee(org_id, offset, limit), many=True).data,
            "total": people.count_employee(org_id)
        }, status=status.HTTP_200_OK)
