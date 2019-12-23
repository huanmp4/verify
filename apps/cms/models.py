from django.db import models

# Create your models here.

class Address(models.Model):
    ip = models.CharField(max_length=20)
    content = models.CharField(max_length=20,default=True)
    country = models.CharField(max_length=10,default=True)
    province = models.CharField(max_length=10,default=True)
    city = models.CharField(max_length=10,default=True)
    isp = models.CharField(max_length=10,default=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =['-pub_time']