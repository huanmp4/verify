from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.URLField()
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    pub_time = models.TimeField(auto_now_add = True)
    author = models.ForeignKey('register.User',on_delete=models.SET_NULL,null= True)


class Category(models.Model):
    name = models.CharField(max_length = 20)
    pub_time2 = models.TimeField(auto_now_add=True,null=True)


class Discover(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('register.User',on_delete=models.SET_NULL,null=True)