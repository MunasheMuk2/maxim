from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path("creator/", views.creator_checkout, name="creator_checkout"),
    path("pro/", views.pro_checkout, name="pro_checkout"),
    path("", views.checkout_page, name="checkout"),  # Optional default
    path("success/", views.checkout_success, name="checkout_success"),
]
