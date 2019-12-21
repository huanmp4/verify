from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from apps.news.models import Discover,News,NewsComment,Banner
from apps.news.forms import DiscoverForm,CommentForm
from utils import restful
from apps.register.models import User
from django.conf import settings
from .serializers import NewsSerializers,NewDetailSerializers,CommentSerializers,BannerSerializers
import time

# Create your views here.

def index(request):
    newses = News.objects.all()[0:1]
    banners = Banner.objects.all()
    context = {'newses':newses,'banners':banners}
    return render(request,'news/index.html',context)



def Discover_Process(request):
    count = settings.PAGE_LOAD_NUM
    if request.method == 'GET':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
            print('IP地址', ip)
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
            print('访客代理ip:', ip)

        log_time = time.strftime(
            '[%Y-%m-%d %H:%M:%S]',
            time.localtime(
                time.time()))  # 转化时间格式
        with open('djangolog.log', 'r') as r:
            Read = r.readlines()

        with open('djangolog.log', 'w') as w:
            w.write("Time:%s,IP:%s\n" % (str(log_time), ip))
            for i in Read:
                w.write(i)

        discover = Discover.objects.all().select_related('author')
        context = {'discover':discover}
        return render(request,'news/discover.html',context)
    else:
        form = DiscoverForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            if str(request.user) != 'AnonymousUser':
                author = request.user
            else:
                exist = User.objects.filter(username='还未注册用户1').exists()
                if exist:
                    author = User.objects.get(username='还未注册用户1')
                else:
                    author = User.objects.create_user(username='还未注册用户1',password=12341234,telephone=13005611199,is_staff=0)
            disc = Discover.objects.create(content=content,author = author)
            disc.save()
            return restful.ok()
        else:
            return restful.params_error('内容或标题不能为空')


def news_list(request):
    num = 1
    p = int(request.GET.get('p',1))
    print('p',p)
    start = (p-1) * settings.PAGE_LOAD_NUM
    end = p * settings.PAGE_LOAD_NUM
    newes = News.objects.order_by('-pub_time')[start:end]
    num += 1
    serializers = NewsSerializers(newes,many=True).data
    content = {'news':serializers}
    return restful.result(data=content)

# def news_detail(request,news_id):
#     category_id = request.GET.get('category_id')
#     news = News.objects.select_related('author','category').get(id=news_id)
#     print('=*10'+'\n')
#     print('=*10'+'\n')
#     context = {'news':news}
#     return render(request,'news/news_detail.html',context = context)

def news_detail(request,news_id):
    category_id = request.GET.get('category_id')
    news = News.objects.prefetch_related('newscomment','author','category').get(id=news_id)
    print('='*10+'\n')
    for i in news.newscomment.all():
        print(i.comment)
    print('='*10+'\n')
    context = {'news':news}
    return render(request,'news/news_detail.html',context = context)

def news_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        news = form.cleaned_data.get('news')
        comment = form.cleaned_data.get('comment')
        if str(request.user) == 'AnonymousUser':
            author = User.objects.get(uid='123123')
        else:
            author = request.user
        print('author',author)
        comments = NewsComment.objects.create(news=news,comment=comment,author=author)
        comments.save()
        data = NewDetailSerializers(comments).data
        print('comments',comments)
        return restful.result(data=data)
    else:
        print('form.get_errors()走到这：',form.get_errors())
        return restful.params_error(form.get_errors())#get_errors()忘记加'()'错过一次


