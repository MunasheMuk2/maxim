from django.contrib import admin
from django.urls import path, include
from home.views import index

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Core Pages
    path("", index, name="home"),
    path("portfolio/", include("portfolio.urls")),
    path("contact/", include("contact.urls")),
    path("faq/", include("faq.urls")),
    # Allauth Authentication
    path("accounts/", include("allauth.urls")),
]
