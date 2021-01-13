from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.models import Course, Tag, CourseTagRef, Teacher, CourseTeacherRef
from assistant.api.v1.serializers.course import CourseSerializer, TagSerializer
from assistant.db.course import get_course_by_id, get_tag_by_id
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

    def post(self, request):
        params = request.data
        org_id = params['org_id']
        course_id = params['course_id']
        if 'tags' in request.data:
            tags = request.data['tags']
        else:
            tags = [params['tag_id']]
        valid_list = []
        course = Course.objects.filter(id=course_id).get()
        for tag_id in tags:
            tag = Tag.objects.filter(id=tag_id).get()
            course_tag_ref = CourseTagRef(course=course, tag=tag, org_id=org_id)
            course_tag_ref.save()
            valid_list.append(tag_id)
        if valid_list:
            return Response(valid_list, status=status.HTTP_201_CREATED)
        return Response(valid_list, status=status.HTTP_400_BAD_REQUEST)


class CourseTeacherApi(MyAPIView):

    def post(self, request):
        params = request.data
        org_id = params['org_id']
        course_id = params['course_id']
        if 'teachers' in request.data:
            teachers = request.data['teachers']
        else:
            teachers = [params['teacher_id']]
        valid_list = []
        course = Course.objects.filter(id=course_id).get()
        for teacher_id in teachers:
            teacher = Teacher.objects.filter(id=teacher_id).get()
            course_teacher_ref = CourseTeacherRef(course=course, teacher=teacher, org_id=org_id)
            course_teacher_ref.save()
            valid_list.append(teacher_id)
        if valid_list:
            return Response(valid_list, status=status.HTTP_201_CREATED)
        return Response(valid_list, status=status.HTTP_400_BAD_REQUEST)