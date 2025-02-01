from django import forms
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

from .models import Url
from .utils import validate_url


class UrlForm(forms.ModelForm):
    custom = forms.CharField(
        max_length=15, required=False, help_text="Optional: Choose a custom short URL"
    )

    class Meta:
        model = Url
        fields = ["long", "custom"]

    def clean_long(self):
        long = self.cleaned_data.get("long")
        if not validate_url(long):
            raise forms.ValidationError("Please enter a valid URL")
        return long

    def clean_custom(self):
        custom = self.cleaned_data.get("custom")
        if custom and Url.objects.filter(short=custom).exists():
            raise ValidationError(
                f"The short URL '{custom}' is already taken. Please choose another one."
            )
        return custom

    def generate_short_url(self):
        # Generates a random 6-character string
        return get_random_string(length=6)

    def save(self, commit=True):
        url_instance = super().save(commit=False)
        custom = self.cleaned_data.get("custom")

        if custom:
            url_instance.short = custom
        else:
            url_instance.short = (
                self.generate_short_url()
            )  # Generate a random short URL if no custom one is provided

        if commit:
            url_instance.save()

        return url_instance
