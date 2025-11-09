import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_page(request):
    return render(request, "checkout/checkout.html")


def checkout_success(request):
    return render(request, "checkout/checkout_success.html")


@login_required
def creator_checkout(request):
    intent = stripe.PaymentIntent.create(
        amount=2000,  # £20.00 in pence
        currency="gbp",
        metadata={"plan": "creator", "user_id": request.user.id},
    )
    return render(
        request,
        "checkout/checkout.html",
        {
            "client_secret": intent.client_secret,
            "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
        },
    )


@login_required
def pro_checkout(request):
    intent = stripe.PaymentIntent.create(
        amount=3900,  # £39.00 in pence
        currency="gbp",
        metadata={"plan": "pro", "user_id": request.user.id},
    )
    return render(
        request,
        "checkout/checkout.html",
        {
            "client_secret": intent.client_secret,
            "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
        },
    )
