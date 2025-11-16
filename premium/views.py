from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PremiumRequest


@login_required
def premium_dashboard(request):
    user = request.user

    if user.plan == "free":
        return redirect("account")

    if request.method == "POST" and user.custom_images_remaining > 0:
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        priority = request.POST.get("priority")

        # Save the request
        PremiumRequest.objects.create(
            user=user,
            title=title,
            description=description,
            category=category,
            priority=priority,
        )

        # Decrement quota
        user.custom_images_remaining -= 1
        user.save()

        # ⭐ Add success message
        messages.success(request, "Your request has been received! 🎉")

        return redirect("premium_dashboard")

    return render(
        request,
        "premium_dashboard.html",
        {
            "remaining": user.custom_images_remaining,
        },
    )
