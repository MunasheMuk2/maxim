from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.premium_content, name="premium_content"),
]
