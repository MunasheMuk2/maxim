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


class CustomRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to="custom_requests/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user.username} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
