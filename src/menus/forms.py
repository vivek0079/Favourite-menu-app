from django import forms

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
