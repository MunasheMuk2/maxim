from django.contrib import admin
from django.urls import path, include
from home.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # Django Allauth
    path(
        "user/", include("accounts.urls")
    ),  # Your custom account views (e.g., premium dashboard)
    path("", index, name="home"),
    path("portfolio/", include("portfolio.urls")),
    path("contact/", include("contact.urls")),
    path("faq/", include("faq.urls")),
    path("", include("home.urls")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
]
