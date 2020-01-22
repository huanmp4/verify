from django.db import models
import shortuuidfield
class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('CourseCategory',on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey("Teacher",on_delete=models.DO_NOTHING)
    video_url = models.URLField()
    cover_url = models.URLField()
    price = models.FloatField()
    duration = models.IntegerField()
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    jobtitle = models.CharField(max_length=100)
    profile = models.TextField()
    avatar = models.URLField()

class CourseCategory(models.Model):
    name = models.CharField(max_length=20)


class CourseOrder(models.Model):
    uid = shortuuidfield.ShortUUIDField(primary_key=True)
    course = models.ForeignKey("Course",on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey("register.User",on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)
    pub_time = models.DateTimeField(auto_now_add=True)
    # 1：代表的是支付宝支付。2：代表的是微信支付
    pay_type = models.SmallIntegerField(default=0)
    # 1：代表的是未支付。2：代表的是支付成功

