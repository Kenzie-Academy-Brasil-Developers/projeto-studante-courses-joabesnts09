from django.db import models
import uuid
 

class StatusChoice(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    status = models.CharField(
        max_length=20, choices=StatusChoice.choices, default=StatusChoice.PENDING
    )

    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
    
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )
