from django import forms
from .models import CreatorApplication


class CreatorApplicationForm(forms.ModelForm):
    class Meta:
        model = CreatorApplication
        fields = ["name", "email", "speciality", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
