from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=20000)

class Category(models.Model):
    name = models.CharField(max_length=20)