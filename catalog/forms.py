from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Cook


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if years_of_experience <= 0:
            raise ValidationError("years_of_experience must be positive")
        return years_of_experience


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search Dish"}),
    )
