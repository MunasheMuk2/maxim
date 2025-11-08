import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_checkout_session(request, plan):
    price_lookup = {
        "creator": "price_1SRHkCBZ2HQQHPr7jdas3J5M",
        "pro": "price_1SRHkcBZ2HQQHPr7Pb7tV17U",
    }

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        customer_email=request.user.email,
        line_items=[
            {
                "price": price_lookup[plan],
                "quantity": 1,
            }
        ],
        mode="subscription",
        success_url=request.build_absolute_uri("/checkout/success/"),
        cancel_url=request.build_absolute_uri("/checkout/cancel/"),
    )
    return redirect(session.url, code=303)
