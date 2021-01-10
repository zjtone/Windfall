from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.employee import EmployeeSerializer
from assistant.db.people import get_employee_by_id
from assistant.api.apiviews import MyAPIView


class EmployeeApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                employee = get_employee_by_id(_id)
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
