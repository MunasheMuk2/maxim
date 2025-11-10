from django.contrib import admin
from django.urls import path, include
from home.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication
    path("accounts/", include("allauth.urls")),  # Django Allauth
    path(
        "user/", include("accounts.urls")
    ),  # Custom account routes (e.g., premium dashboard)
    # Core Pages
    path("", index, name="home"),
    path("portfolio/", include("portfolio.urls")),
    path("contact/", include("contact.urls")),
    path("faq/", include("faq.urls")),
    path("", include("home.urls")),
    # Checkout / Payments
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("user/", include("accounts.urls")),
]
