from django import forms
from .models import Category, Location


class HolidayFilterForm(forms.Form):
    category = forms.ChoiceField(choices=[], required=False)
    location = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super(HolidayFilterForm, self).__init__(*args, **kwargs)
        self.fields["category"].choices = [
            (category.id, category.name) for category in Category.objects.all()
        ]
        self.fields["location"].choices = [
            (location.id, location.name) for location in Location.objects.all()
        ]
