from django.urls import path
from .views import creator_checkout, pro_checkout, checkout_success, checkout_cancel

app_name = "checkout"

urlpatterns = [
    path("creator/", creator_checkout, name="creator_checkout"),
    path("pro/", pro_checkout, name="pro_checkout"),
    path("success/", checkout_success, name="checkout_success"),
    path("cancel/", checkout_cancel, name="checkout_cancel"),
]
