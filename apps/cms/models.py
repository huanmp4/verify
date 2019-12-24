from django.db import models

# Create your models here.

class Address(models.Model):
    ip = models.CharField(max_length=20)
    content = models.CharField(max_length=20,default='null')
    country = models.CharField(max_length=10,default='null')
    province = models.CharField(max_length=10,default='null')
    city = models.CharField(max_length=10,default='null')
    isp = models.CharField(max_length=10,default='null')
    pub_time = models.DateTimeField(auto_now_add='null')
    class Meta:
        ordering =['-pub_time']