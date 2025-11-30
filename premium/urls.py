from django.urls import path
from .views import premium_dashboard
from . import views

urlpatterns = [
    path("", premium_dashboard, name="premium_dashboard"),
    path("request/<int:pk>/edit/", views.edit_request, name="edit_request"),
    path("request/<int:pk>/delete/", views.delete_request, name="delete_request"),
]
