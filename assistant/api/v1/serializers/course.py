from assistant.models import Course, Tag, CourseTagRef, CourseTeacherRef
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


class CourseSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'org_id', 'status',
                  'name', 'description', 'img', 'price', 'capacity',
                  'tags', 'teachers']