from django.db import models
import uuid


class StatusChoice(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20, choices=StatusChoice.choices, default=StatusChoice.NOT_STARTED
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="courses"
    )

    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
