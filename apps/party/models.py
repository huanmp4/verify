from django.db import models

# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=200,default='空')
    cellphone = models.CharField(max_length=200,default='空')
    memo = models.CharField(max_length=200,default='空')
    money = models.CharField(max_length=200,default='')

