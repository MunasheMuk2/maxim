from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PremiumRequest


@login_required
def premium_dashboard(request):
    user = request.user

    if user.plan == "free":
        return redirect("account")

    # Handle new request creation
    if request.method == "POST":
        if user.custom_images_remaining <= 0:
            messages.error(request, "You’ve used all your custom requests.")
            return redirect("premium_dashboard")

        title = (request.POST.get("title") or "").strip()
        description = (request.POST.get("description") or "").strip()
        category = request.POST.get("category")
        priority = request.POST.get("priority")

        allowed_categories = dict(PremiumRequest.CATEGORY_CHOICES).keys()
        allowed_priorities = dict(PremiumRequest.PRIORITY_CHOICES).keys()

        if not title or not description:
            messages.error(request, "Title and description are required.")
        elif category not in allowed_categories or priority not in allowed_priorities:
            messages.error(request, "Invalid category or priority.")
        else:
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
    requests_qs = PremiumRequest.objects.filter(user=user).order_by("-created_at")

    return render(
        request,
        "premium_dashboard.html",
        {
            "remaining": user.custom_images_remaining,
            "requests": requests_qs,
        },
    )


@login_required
def edit_request(request, pk):
    req = get_object_or_404(PremiumRequest, pk=pk, user=request.user)

    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        description = (request.POST.get("description") or "").strip()
        category = request.POST.get("category")
        priority = request.POST.get("priority")

        allowed_categories = dict(PremiumRequest.CATEGORY_CHOICES).keys()
        allowed_priorities = dict(PremiumRequest.PRIORITY_CHOICES).keys()

        if not title or not description:
            messages.error(request, "Title and description are required.")
        elif category not in allowed_categories or priority not in allowed_priorities:
            messages.error(request, "Invalid category or priority.")
        else:
            req.title = title
            req.description = description
            req.category = category
            req.priority = priority
            req.save()
            messages.success(request, "Request updated successfully!")
            return redirect("edit_request", pk=req.pk)

    # Fetch all requests for display in the edit page
    all_requests = PremiumRequest.objects.filter(user=request.user).order_by(
        "-created_at"
    )

    return render(
        request,
        "edit_request.html",
        {
            "request_obj": req,
            "requests": all_requests,
        },
    )


@login_required
def delete_request(request, pk):
    req = get_object_or_404(PremiumRequest, pk=pk, user=request.user)

    if request.method == "POST":
        req.delete()
        messages.success(request, "Request deleted successfully!")
        return redirect(
            "edit_request", pk=pk
        )  # Redirect to edit page (may need adjustment)

    return render(request, "confirm_delete_request.html", {"request_obj": req})
