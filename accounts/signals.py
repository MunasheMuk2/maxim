from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def set_default_plan(sender, instance, created, **kwargs):
    if created and not instance.plan:
        instance.plan = "free"
        instance.custom_images_remaining = 5
        instance.save()
