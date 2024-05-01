from queue import Full
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())