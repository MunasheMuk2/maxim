from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_page(request):
    return render(request, "checkout/checkout.html")


@login_required
def premium_content(request):
    user = request.user
    profile = user.userprofile

    # Block if out of requests
    if profile.custom_requests_remaining < 1:
        message = (
            "You've used all your custom requests. Wait for next month or upgrade."
        )
        return render(
            request,
            "accounts/premium_dashboard.html",
            {"form": None, "message": message, "profile": profile},
        )

    if request.method == "POST":
        form = CustomRequestForm(request.POST, request.FILES)
        if form.is_valid():
            custom_request = form.save(commit=False)
            custom_request.user = user
            custom_request.save()
            profile.custom_requests_remaining -= 1
            profile.save()
            return redirect("premium_content")
    else:
        form = CustomRequestForm()

    return render(
        request, "accounts/premium_dashboard.html", {"form": form, "profile": profile}
    )
