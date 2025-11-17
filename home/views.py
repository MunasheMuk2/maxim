from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CreatorApplication


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        speciality = request.POST.get("speciality")
        message_text = request.POST.get("message")

        CreatorApplication.objects.create(
            name=name,
            email=email,
            speciality=speciality,
            message=message_text,
        )

        messages.success(request, "Thank you! Your application has been received.")
        return redirect("/#main-content")  # Redirect back to the form section

    return render(request, "index.html")
