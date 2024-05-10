from rest_framework import serializers
from students_courses.serializers import StudentSerializer
from .models import Course



class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        read_only_fields = ["contents"]

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    