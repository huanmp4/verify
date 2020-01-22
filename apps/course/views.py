
from django.shortcuts import render,reverse,redirect
from apps.course.models import Course,Teacher,CourseCategory
from django.views.generic import View
from utils import restful
from .models import CourseOrder
def course_index(request):
    course = Course.objects.all()
    context = {'courses':course}
    return render(request,'course/course_index.html',context=context)


def course_detail(request,course_id):
    course = Course.objects.get(pk=course_id)
    try:
        buyed = CourseOrder.objects.filter(course=course,buyer=request.user).exists()
        print('buyed' + buyed)
        context = {
            'course': course,
            'buyed': buyed
        }
        return render(request, 'course/course_detail.html', context=context)
    except:
        return render(request, 'course/course_detail.html', {'course':course})


def course_token(request):
    import hmac, os
    import time, datetime
    import hashlib
    file = request.GET.get('video')
    UserKey = 'c982d508182a4fb6'
    UserKey = UserKey.encode('utf-8')
    userid = '9b594b02a300443eb23fdb723ef74f68'
    mediald = 'http://jmrcwcw03u4rd6ptgzj.exp.bcevod.com/mda-jmssk05f5a834fdh/mda-jmssk05f5a834fdh.m3u8'
    extension = os.path.splitext(mediald)[1]
    mediald = mediald.split('/')[-1].replace('.m3u8', '')
    expiration = int(time.time()) + (60 * 60 * 2)
    media_and_time = '/{0}/{1}'.format(mediald, expiration).encode('utf-8')
    signature = hmac.new(UserKey, media_and_time, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, userid, expiration)
    print('signature', signature)
    print('mediald', mediald)
    print('extension', extension)
    print('media_and_time', media_and_time)
    print('token', token)
    return restful.result(data={'token':token})



def course_order_key(request):
    from hashlib import md5
    import requests
    from django.http import HttpResponseRedirect
    course_id = request.GET.get('course_id')
    course_name = request.GET.get('course_name')
    istype = request.GET.get('istype')
    price = request.GET.get('price')
    order = request.GET.get('orderid')
    print('course_id',course_id)
    print('course_name',course_name)
    print('istype',istype)
    print('price',price)
    print('order',order)

    url = 'https://pay.bearsoftware.net.cn/'
    uid = 'a274021ea646ce998bdc88c6'
    token = '36f7e6d640dcbf55bdbcdd6adeaee7ef'
    orderid = order
    orderuid = str(request.user.pk)
    print('orderuid',orderuid)
    istype =istype
    #用户支付成功后，我们服务器会主动发送一个post消息到这个网址。
    notify_url = request.build_absolute_uri(reverse('course:notify_view'))
    print('notify_url'+notify_url)
    #用户支付成功后，我们会让用户浏览器自动跳转到这个网址。
    return_url = request.build_absolute_uri(reverse('course:course_detail',kwargs={'course_id':course_id}))
    print('return_url',return_url)
    #商品名称
    goodsname = course_name
    #把使用到的所有参数，连Token一起，按参数名字母升序排序。把参数值拼接在一起。做md5-32位加密，取字符串小写。
    #就按这个顺序拼接：goodsname + istype + notify_url + orderid + orderuid + price + return_url + token + uid
    key = md5((course_name + istype + notify_url + orderid + orderuid  + price + return_url + token + uid).encode('utf-8')).hexdigest()
    params = {
        'uid':uid,
        'price':float(price),
        'istype':int(istype),
        'notify_url':notify_url,
        'return_url':return_url,
        'orderid':orderid,
        'orderuid':orderuid,
        'goodsname':goodsname,
        'key':key
    }
    return restful.result(data=params)
def notify_view(request):
    order_id = request.POST.get('orderid')
    print('notify_view',order_id)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def login_requireds(request):
    return HttpResponse('请登录')

@login_required(login_url='/course/login_requireds')
def course_pay(request,course_id):
    course = Course.objects.get(pk = course_id)
    print(' course_pay course'+ course.title)
    order = CourseOrder.objects.create(course=course,buyer=request.user,amount=course.price)
    context = {
        'goods':course,
        'order':order
    }
    return render(request,'course/course_pay.html',context=context)