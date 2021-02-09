from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.teacher import TeacherSerializer
from assistant.db import people
from assistant.api.apiviews import MyAPIView


class TeacherApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                teacher = people.get_teacher_by_id(_id)
                return Response(TeacherSerializer(teacher).data)
            raise Http404
        except Exception as e:
            print('[TeacherApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        params = request.data
        if "id" in params:
            return TeacherApi.update(request)
        serializer = TeacherSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if "id" in params:
                update_teacher = request.data
                exist_teacher = people.get_teacher_by_id(params["id"])
                for key in update_teacher:
                    if hasattr(exist_teacher, key):
                        setattr(exist_teacher, key, update_teacher[key])
                exist_teacher.save()
                return Response("", status=status.HTTP_200_OK)
            raise Http404
        except Exception as e:
            raise Http404


class TeacherList(MyAPIView):
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
            "data": TeacherSerializer(people.list_teacher(org_id, offset, limit), many=True).data,
            "total": people.count_teacher(org_id)
        }, status=status.HTTP_200_OK)
