from django import forms
from utils import restful

class NewsForm(forms.Form,restful.FormError):
    name = forms.CharField()
    content = forms.CharField()

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=30)


