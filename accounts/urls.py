from django.urls import path
from .views import account_view, cancel_plan, upgrade_plan

urlpatterns = [
    path("account/", account_view, name="account"),
    path("account/cancel/", cancel_plan, name="account_cancel"),
    path("account/upgrade/", upgrade_plan, name="account_upgrade"),
]
