from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from assistant.models import Course, Tag, CourseTagRef, Teacher, CourseTeacherRef
from assistant.api.v1.serializers.course import CourseSerializer, TagSerializer, CourseTimeRefSerializer, \
    TimeSerializer, CourseTagSerializer, CourseTeacherSerializer
from assistant.api.v1.serializers.teacher import TeacherSerializer
from assistant.db import course, people
from assistant.api.apiviews import MyAPIView


class CourseApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                data = CourseSerializer(course.get_course_by_id(params["id"])).data
                # 查询课程的标签
                course_tag_refs = [c_tag.tag_id for c_tag in course.get_tag_ref_by_course_id(params["id"])]
                data.update({"tags": TagSerializer(course.list_tag_by_id(course_tag_refs), many=True).data})
                # 查询课程相关的教师
                course_teacher_refs = [c_teacher["teacher_id"] for c_teacher in course.get_teacher_ref_by_course_id(params["id"])]
                data.update({"teachers": TeacherSerializer(people.list_teacher_by_id(course_teacher_refs), many=True).data})
                # 查询课程排课的时间
                course_time_refs = [c_time["time_id"] for c_time in course.get_time_ref_by_course_id(params["id"])]
                data.update({"times": TimeSerializer(course.list_time_by_id(course_time_refs), many=True).data})
                return Response(data)
            raise Http404
        except Exception as e:
            print('[CourseApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        params = request.data
        if "id" in params:
            return CourseApi.update(request)
        refs = {
            "tag": CourseTagSerializer,
            "teacher": CourseTeacherSerializer,
            "time": CourseTimeRefSerializer
        }
        serializer = CourseSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            if "tags" in params:
                course.course_tags(serializer.data["id"], params["tags"], serializer.data["org_id"])
            if "teachers" in params:
                course.course_teachers(serializer.data["id"], params["teachers"], serializer.data["org_id"])
            if "times" in params:
                course.course_times(serializer.data["id"], params["times"], serializer.data["org_id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if "id" in params:
                update_course = request.data
                exist_course = course.get_course_by_id(params["id"])
                for key in update_course:
                    if key == "tags":
                        course.course_tags(serializer.data["id"], params["tags"], serializer.data["org_id"])
                    elif key == "teachers":
                        course.course_teachers(serializer.data["id"], params["teachers"], serializer.data["org_id"])
                    elif key == "times":
                        course.course_times(serializer.data["id"], params["times"], serializer.data["org_id"])
                    elif hasattr(exist_course, key):
                        setattr(exist_course, key, update_course[key])
                exist_course.save()
                return Response("", status=status.HTTP_200_OK)
            raise Http404
        except Exception as e:
            print("e ", e)
            raise Http404


class TagApi(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                return Response(TagSerializer(course.get_tag_by_id(params["id"])).data)
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


class TagList(MyAPIView):

    def get(self, request):
        try:
            params = request.data
            org_id = params['org_id']
            return Response(TagSerializer(course.list_tag(org_id), many=True).data,
                            status=status.HTTP_200_OK)
        except Exception as e:
            print('[TagList]get e = {}'.format(e))
            raise Http404


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


class CourseList(MyAPIView):
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
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None
        course_list = course.list_course(org_id, offset, limit, data_status)
        return Response({
            "data": CourseSerializer(course_list, many=True).data,
            "total": course.count_course(org_id, data_status)
        }, status=status.HTTP_200_OK)


class CourseTimeRefApi(MyAPIView):
    def post(self, request):
        serializer = CourseTimeRefSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeApi(MyAPIView):
    def post(self, request):
        serializer = TimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
