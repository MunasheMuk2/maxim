from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def premium_dashboard(request):
    if request.user.plan == "free":
        return redirect("account")

    return render(
        request,
        "premium_dashboard.html",
        {"remaining": request.user.custom_images_remaining},
    )
