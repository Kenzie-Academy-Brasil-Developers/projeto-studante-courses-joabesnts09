from django.urls import path
from .views import CreateContentView, GetUpdateDeleteContentView


urlpatterns = [
    path("courses/<uuid:course_id>/contents/", CreateContentView.as_view()),
    path(
        "courses/<uuid:course_id>/contents/<uuid:content_id>/",
        GetUpdateDeleteContentView.as_view(),
    ),
]
