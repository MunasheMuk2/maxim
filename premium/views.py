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

        PremiumRequest.objects.create(
            user=user,
            title=title,
            description=description,
            category=category,
            priority=priority,
        )

        user.custom_images_remaining -= 1
        user.save()

        messages.success(request, "Your request has been received!")
        return redirect("premium_dashboard")

    # Fetch all requests for this user
    requests = PremiumRequest.objects.filter(user=user).order_by("-created_at")

    return render(
        request,
        "premium_dashboard.html",
        {
            "remaining": user.custom_images_remaining,
            "requests": requests,
        },
    )


@login_required
def edit_request(request, pk):
    req = PremiumRequest.objects.get(pk=pk, user=request.user)

    if request.method == "POST":
        req.title = request.POST.get("title")
        req.description = request.POST.get("description")
        req.category = request.POST.get("category")
        req.priority = request.POST.get("priority")
        req.save()

        messages.success(request, "Request updated successfully!")
        return redirect("premium_dashboard")

    return render(request, "edit_request.html", {"request_obj": req})


@login_required
def delete_request(request, pk):
    req = PremiumRequest.objects.get(pk=pk, user=request.user)
    req.delete()
    messages.success(request, "Request deleted successfully!")
    return redirect("premium_dashboard")
