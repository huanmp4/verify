from rest_framework import serializers
from .models import News,Category,Discover,NewsComment,Banner
from apps.register.serializers import UserSerializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class NewsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    author = UserSerializers()
    class Meta:
        model = News
        fields = ('id','title','content','pub_time','category','author','thumbnail')


class CommentSerializers(serializers.ModelSerializer):
    author = UserSerializers()
    class Meta:
        model = Discover
        fields = ('content','pub_time')

class NewDetailSerializers(serializers.ModelSerializer):
    author = UserSerializers()
    class Meta:
        model = NewsComment
        fields = '__all__'


class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'