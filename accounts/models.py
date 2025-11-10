from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    SUBSCRIPTION_CHOICES = [
        ("free", "Free"),
        ("creator", "Creator"),
        ("pro", "Pro"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_level = models.CharField(
        max_length=20, choices=SUBSCRIPTION_CHOICES, default="free"
    )
    custom_requests_remaining = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_level}"
