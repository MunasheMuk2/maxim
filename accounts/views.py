from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def account_view(request):
    return render(
        request,
        "account.html",
        {
            "plan": request.user.plan,
            "remaining": request.user.custom_images_remaining,
        },
    )


# Cancel current plan
@login_required
def cancel_plan(request):
    user = request.user
    user.plan = "free"
    user.custom_images_remaining = 0
    user.save()
    return redirect("account")


# Upgrade to Pro (redirect to Stripe checkout)
@login_required
def upgrade_plan(request):
    return redirect("checkout:pro_checkout")
