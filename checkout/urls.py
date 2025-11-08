from django.urls import path
from . import views

app_name = "checkout"  # ✅ This defines the namespace!

urlpatterns = [
    path("<str:plan>/", views.create_checkout_session, name="create_checkout_session"),
    path("success/", views.checkout_success, name="checkout_success"),
]
