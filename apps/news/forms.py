
from django import forms
from .models import Discover

class DiscoverForm(forms.ModelForm):
    class Meta:
        model = Discover
        exclude = ['pub_time','author']