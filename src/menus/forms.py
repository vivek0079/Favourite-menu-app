from django import forms

from restaurants.models import Restaurant
from .models import Item

class ItemForm(forms.ModelForm):
    """Form definition for Item."""

    class Meta:
        """Meta definition for Itemform."""

        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public',
        ]
    def __init__(self, user=None, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)