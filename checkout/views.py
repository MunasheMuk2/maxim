import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def creator_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": "price_1SRHkCBZ2HQQHPr7jdas3J5M",  # Replace with your Stripe price ID
                "quantity": 1,
            }
        ],
        mode="subscription",
        success_url=request.build_absolute_uri("/checkout/success/?plan=creator"),
        cancel_url=request.build_absolute_uri("/checkout/cancel/"),
        customer_email=request.user.email,
    )
    return redirect(session.url)


@login_required
def pro_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": "price_1SRHkcBZ2HQQHPr7Pb7tV17U",  # Replace with your Stripe price ID
                "quantity": 1,
            }
        ],
        mode="subscription",
        success_url=request.build_absolute_uri("/checkout/success/?plan=pro"),
        cancel_url=request.build_absolute_uri("/checkout/cancel/"),
        customer_email=request.user.email,
    )
    return redirect(session.url)


@login_required
def checkout_success(request):
    plan = request.GET.get("plan")
    user = request.user

    if plan == "creator":
        user.plan = "creator"
        user.custom_images_remaining = 3
    elif plan == "pro":
        user.plan = "pro"
        user.custom_images_remaining = 5

    user.save()
    return redirect("premium_dashboard")


@login_required
def checkout_cancel(request):
    return redirect("account")
