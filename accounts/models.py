from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    PLAN_CHOICES = [
        ("free", "Free"),
        ("creator", "Creator Access"),
        ("pro", "Pro Access"),
    ]
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default="free")
    custom_images_remaining = models.IntegerField(default=0)
