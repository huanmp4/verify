from django.db import models

# Create your models here.

class Address(models.Model):
    ip = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =['-pub_time']