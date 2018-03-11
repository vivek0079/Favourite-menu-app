from django import forms

from .models import Restaurant
from .validators import validate_category

class RestaurantForm(forms.Form):
    """RestaurantForm definition."""
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

class RestaurantCreateForm(forms.ModelForm):
    """Form definition for Restaurant."""
    class Meta:
        """Meta definition for Restaurantform."""
        model = Restaurant
        fields = [
            'name',
            'location',
            'category',
        ]
