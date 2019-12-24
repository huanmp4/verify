from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from apps.news.models import News,NewsComment,Banner
from apps.news.forms import CommentForm
from utils import restful
from apps.register.models import User
from django.conf import settings
from .serializers import NewsSerializers,NewDetailSerializers,CommentSerializers,BannerSerializers


# Create your views here.

def index(request):
    newses = News.objects.all()[0:settings.PAGE_LOAD_NUM]
    banners = Banner.objects.all()
    context = {'newses':newses,'banners':banners}
    restful.get_address(request,'进入到主页')
    return render(request,'news/index.html',context)

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


