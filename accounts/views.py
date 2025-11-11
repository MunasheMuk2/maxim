from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def premium_content(request):
    profile = request.user.userprofile
    if profile.subscription_level == "free":
        message = "Upgrade to access premium content."
    else:
        message = None

    return render(
        request,
        "accounts/premium_dashboard.html",
        {
            "form": None,  # Replace with your form
            "message": message,
            "profile": profile,
        },
    )
