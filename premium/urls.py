from django.urls import path
from .views import premium_dashboard

urlpatterns = [
    path("", premium_dashboard, name="premium_dashboard"),
]
