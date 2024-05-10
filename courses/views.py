from rest_framework import generics
from courses.serializers import Course, CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from courses.permissions import CoursePermission
from students_courses.serializers import StudentCourseSerializer


class CreateListCourseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CoursePermission]
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        
        return self.queryset.filter(students=self.request.user)
    

class GetUpdateDeleteCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CoursePermission]
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'course_id'


class GetUpdateStudentView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CoursePermission]
    
    serializer_class = StudentCourseSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = 'course_id'
    