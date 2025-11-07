from django.contrib import admin
from .models import CreatorApplication

# Register your models here.


@admin.register(CreatorApplication)
class CreatorApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "speciality", "created_at")
    search_fields = ("name", "email", "speciality")
