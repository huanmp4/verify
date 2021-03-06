from django import forms
from utils.restful import FormError
from utils import restful
from apps.course.models import Course
from apps.news.models import News,Banner


class NewsForm(forms.ModelForm,FormError):
    category = forms.IntegerField()
    class Meta:
        model = News
        fields = ('title','content','thumbnail')



class CategoryForm(forms.Form,FormError):
    id = forms.CharField(max_length=20,required=False)
    name = forms.CharField(max_length=30)


class BannerForm(forms.ModelForm,FormError):
    banner_id = forms.IntegerField(required=False)
    class Meta:
        model = Banner
        fields = '__all__'

class PubCourseForm(forms.ModelForm,FormError):
    category_id = forms.IntegerField()
    teacher_id = forms.IntegerField()
    class Meta:
        model = Course
        exclude = ("category",'teacher')