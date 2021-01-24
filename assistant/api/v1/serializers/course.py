from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef, CourseTimeRef, Time
from assistant.api.v1.serializers.teacher import TeacherSerializer
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'org_id', 'status', 'name']


class CourseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTagRef
        fields = ['id', 'org_id', 'status', 'course_id', 'tag_id']


class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacherRef
        fields = ['id', 'org_id', 'status', 'course_id', 'teacher_id']


class CourseTimeRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTimeRef
        fields = ['id', 'org_id', 'status', 'course_id', 'time_id']


class CourseSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    teachers = TeacherSerializer(many=True)
    times = CourseTimeRefSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'org_id', 'status',
                  'name', 'description', 'img', 'price', 'capacity',
                  'tags', 'teachers', 'start_time', 'end_time',
                  'times']


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'org_id', 'status',
                  'start_time', 'end_time']
