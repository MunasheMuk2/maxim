# checkout/views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def creator_checkout(request):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=2000,  # £20 -> in pence
            currency="gbp",
            metadata={"plan": "creator"},
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


@login_required
def pro_checkout(request):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=3900,  # £39 -> in pence
            currency="gbp",
            metadata={"plan": "pro"},
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


@csrf_exempt
@login_required
def checkout_success(request):
    user = request.user
    profile = user.userprofile
    plan = request.GET.get("plan")

    if plan == "creator":
        profile.subscription_level = "creator"
        profile.custom_requests_remaining = 3
    elif plan == "pro":
        profile.subscription_level = "pro"
        profile.custom_requests_remaining = 5

    profile.save()
    return redirect("checkout:premium_content")


@login_required
def premium_content(request):
    return render(request, "checkout/premium_dashboard.html")  # Create this template
