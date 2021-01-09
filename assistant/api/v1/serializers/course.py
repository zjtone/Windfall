from assistant.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'org_id', 'status',
                  'name', 'description', 'img', 'price', 'capacity']
