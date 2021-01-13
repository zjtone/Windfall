from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'org_id', 'status',
                  'name', 'description', 'img', 'price', 'capacity']


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
