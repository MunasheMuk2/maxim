from django.urls import path
from .views import account_view, cancel_plan, upgrade_plan

urlpatterns = [
    path("account/", account_view, name="account"),
    path("account/cancel/", cancel_plan, name="cancel_plan"),
    path("account/upgrade/", upgrade_plan, name="upgrade_plan"),
]
