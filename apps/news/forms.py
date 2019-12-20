
from django import forms
from .models import Discover,NewsComment,Banner
from utils.restful import FormError
from .formErrors import FormMixin2
class DiscoverForm(forms.ModelForm):
    class Meta:
        model = Discover
        exclude = ['pub_time','author']


class CommentForm(forms.ModelForm,FormError):
    class Meta:
        model = NewsComment
        exclude = ['author']
        error_messages = {
            'comment':{
                'max_length':'不能大于10个字符',
                'required': '内容不能为空哦'
            },
        }


