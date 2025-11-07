from django import forms
from .models import CreatorApplication


class CreatorApplicationForm(forms.ModelForm):
    class Meta:
        model = CreatorApplication
        fields = ["name", "email", "speciality", "message"]
