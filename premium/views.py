@login_required
def edit_request(request, pk):
    req = get_object_or_404(PremiumRequest, pk=pk, user=request.user)
    requests_qs = PremiumRequest.objects.filter(user=request.user).order_by(
        "-created_at"
    )

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
            return redirect("edit_request", pk=pk)

    return render(
        request,
        "edit_request.html",
        {
            "request_obj": req,
            "requests": requests_qs,
        },
    )
