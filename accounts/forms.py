from django import forms
from .models import CustomRequest


class CustomRequestForm(forms.ModelForm):
    class Meta:
        model = CustomRequest
        fields = ["message", "image"]
        widgets = {
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
