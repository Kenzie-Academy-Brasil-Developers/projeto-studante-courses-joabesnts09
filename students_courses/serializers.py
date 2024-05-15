from rest_framework import serializers
from courses.models import Course
from accounts.models import Account
from .models import StudentCourse


class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='student.id', read_only=True)
    student_username = serializers.CharField(source='student.username', read_only=True)
    student_email = serializers.CharField(source='student.email')
    

    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'student_username', 'student_email', 'status']

        

class StudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentSerializer(many=True)
    
    class Meta:
        model = Course
        fields = ['id','name', 'students_courses']
        read_only_fields = ['id','name']
    
    
    def update(self, instance, validated_data):
        students = []
        students_not_found = []

        for students_courses in validated_data['students_courses']:
            student_email = students_courses['student']['email']
            student = Account.objects.filter(email=student_email).first()
            
            if not student:
                students_not_found.append(student_email)
            else:
                students.append(student)
                
        
        if len(students_not_found):
            raise serializers.ValidationError({'detail': f"No active accounts was found: {', '.join(students_not_found)}."})
        
        instance.students.add(*students)
        return instance