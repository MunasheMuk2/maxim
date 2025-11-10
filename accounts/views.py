from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_page(request):
    return render(request, "checkout/checkout.html")


@login_required
def premium_content(request):
    return render(request, "accounts/premium_dashboard.html")
