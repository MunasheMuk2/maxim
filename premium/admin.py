from django.contrib import admin
from .models import PremiumRequest


@admin.register(PremiumRequest)
class PremiumRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "priority", "created_at")
    search_fields = ("title", "user__username", "description")
