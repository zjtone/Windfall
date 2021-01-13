from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.course import CourseSerializer, TagSerializer, \
    CourseTagSerializer, CourseTeacherSerializer
from assistant.api.v1.serializers.teacher import TeacherSerializer
from assistant.db.course import get_course_by_id, get_tag_by_id, course_to_tag, course_to_teacher
from assistant.api.apiviews import MyAPIView


class CourseApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                return Response(CourseSerializer(get_course_by_id(params["id"])).data)
            raise Http404
        except Exception as e:
            print('[CourseApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                return Response(TagSerializer(get_tag_by_id(params["id"])).data)
            raise Http404
        except Exception as e:
            print('[TagApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseTagApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "course_id" in params:
                return Response(TagSerializer(course_to_tag(params["course_id"]), many=True).data)
            raise Http404
        except Exception as e:
            print('[CourseTagApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        if 'list' in request.data:
            data_list = request.data['list']
        else:
            data_list = [request.data]
        valid_list = []
        for data in data_list:
            serializer = CourseTagSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                valid_list.append(serializer.data)
        if valid_list:
            return Response(valid_list, status=status.HTTP_201_CREATED)
        return Response(valid_list, status=status.HTTP_400_BAD_REQUEST)


class CourseTeacherApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "course_id" in params:
                return Response(TeacherSerializer(course_to_teacher(params["course_id"]), many=True).data)
            raise Http404
        except Exception as e:
            print('[CourseTeacherApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        if 'list' in request.data:
            data_list = request.data['list']
        else:
            data_list = [request.data]
        valid_list = []
        for data in data_list:
            serializer = CourseTeacherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                valid_list.append(serializer.data)
        if valid_list:
            return Response(valid_list, status=status.HTTP_201_CREATED)
        return Response(valid_list, status=status.HTTP_400_BAD_REQUEST)
