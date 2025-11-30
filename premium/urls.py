from django.urls import path
from .views import premium_dashboard, edit_request, delete_request

urlpatterns = [
    path("", premium_dashboard, name="premium_dashboard"),
    path("request/<int:pk>/edit/", edit_request, name="edit_request"),
    path("request/<int:pk>/delete/", delete_request, name="delete_request"),
]
