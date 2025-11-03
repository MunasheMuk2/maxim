from django.urls import path
from .views import faq

urlpatterns = [
    path("", faq_view, name="faq"),
]
