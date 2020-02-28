from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.URLField()
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    pub_time = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('register.User',on_delete=models.SET_NULL,null= True)
    class Meta:
        ordering = ['-pub_time']

class Category(models.Model):
    name = models.CharField(max_length = 20)
    pub_time2 = models.DateTimeField(auto_now_add=True,null=True)


class Discover(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('register.User',on_delete=models.SET_NULL,null=True)

class NewsComment(models.Model):
    news = models.ForeignKey('News',on_delete=models.CASCADE,null=True,related_name='newscomment')
    comment = models.TextField(max_length=200)
    pub_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('register.User',on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering = ['-pub_time']


class Banner(models.Model):
    link_to = models.CharField(max_length=300)
    priority = models.IntegerField()
    image_url = models.URLField()
    pub_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-priority']
