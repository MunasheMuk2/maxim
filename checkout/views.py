from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from accounts.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def creator_checkout(request):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=2000, currency="gbp", metadata={"plan": "creator"}
        )
        return render(
            request,
            "checkout/checkout.html",
            {
                "client_secret": intent.client_secret,
                "plan": "creator",
                "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
            },
        )
    return render(request, "checkout/checkout.html", {"plan": "creator"})


@login_required
def pro_checkout(request):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=3900, currency="gbp", metadata={"plan": "pro"}
        )
        return render(
            request,
            "checkout/checkout.html",
            {
                "client_secret": intent.client_secret,
                "plan": "pro",
                "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
            },
        )
    return render(request, "checkout/checkout.html", {"plan": "pro"})


@login_required
def checkout_success(request):
    plan = request.GET.get("plan", "")
    profile = request.user.userprofile

    if plan == "creator":
        profile.subscription_level = "creator"
        profile.custom_requests_remaining = 3
    elif plan == "pro":
        profile.subscription_level = "pro"
        profile.custom_requests_remaining = 5
    else:
        # fallback to free
        profile.subscription_level = "free"
        profile.custom_requests_remaining = 0

    profile.save()
    return redirect("premium_content")  # Ensure this URL is correctly named
