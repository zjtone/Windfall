from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.teacher import TeacherSerializer
from assistant.db.people import get_teacher_by_id
from assistant.api.apiviews import MyAPIView


class TeacherApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                teacher = get_teacher_by_id(_id)
                return Response(TeacherSerializer(teacher).data)
            raise Http404
        except Exception as e:
            print('[TeacherApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
