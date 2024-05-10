from django.urls import path
from .views import CreateListCourseView, GetUpdateDeleteCourseView, GetUpdateStudentView


urlpatterns = [
    path('courses/', CreateListCourseView.as_view()),
    path('courses/<uuid:course_id>/', GetUpdateDeleteCourseView.as_view()),
    path('courses/<uuid:course_id>/students/', GetUpdateStudentView.as_view()),

]
