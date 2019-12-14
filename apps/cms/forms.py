from django import forms
from utils import restful
from apps.news.models import News

class NewsForm(forms.ModelForm,restful.FormError):
    category = forms.IntegerField()
    class Meta:
        model = News
        fields = ('title','content','thumbnail')



class CategoryForm(forms.Form,restful.FormError):
    id = forms.CharField(max_length=20,required=False)
    name = forms.CharField(max_length=30)


