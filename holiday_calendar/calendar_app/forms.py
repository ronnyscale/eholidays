# forms.py

from django import forms
from .models import Category, Location


class HolidayFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Все категории", required=False
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        empty_label="Все местоположения",
        required=False,
    )
