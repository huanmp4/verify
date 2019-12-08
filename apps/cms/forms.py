from django import forms
from utils import restful

class NewsForm(forms.Form,restful.FormError):
    name = forms.CharField()
    content = forms.CharField()

class CategoryForm(forms.Form,restful.FormError):
    id = forms.CharField(max_length=20,required=False)
    name = forms.CharField(max_length=30)


