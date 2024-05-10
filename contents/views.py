from rest_framework import generics
from contents.models import Content
from contents.serializers import ContentSerializer, Content
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from contents.permissions import ContentPermission
from courses.models import Course


class CreateContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ContentPermission]

    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        found_course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
        return serializer.save(course=found_course)


class GetUpdateDeleteContentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ContentPermission]

    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_id"

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        content_id = self.kwargs.get("content_id")

        if not Course.objects.filter(id=course_id).exists():
            raise Http404({"detail": "course not found."})

        if not Content.objects.filter(id=content_id).exists():
            raise Http404({"detail": "content not found."})

        if self.request.user.is_superuser:
            return self.queryset.filter()

        if not self.queryset.filter(course__in=self.request.user.my_courses.all()):
            raise PermissionDenied

        return self.queryset.filter(course__in=self.request.user.my_courses.all())
