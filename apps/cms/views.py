from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from ..news.models import News
from utils import restful
from .forms import CategoryForm,NewsForm,BannerForm
from apps.news.models import Category,Banner
import os,time
from django.conf import settings
from qiniu import Auth as qiniuAuth
from apps.news.serializers import BannerSerializers

# Create your views here.
def home(request):
    return render(request, 'cms/news/home.html')

def news_release(request):
    return render(request,'cms/news/release.html')

def news_preview(request):
    return render(request,'cms/news/news_preview.html')

class ReleaseNews(View):
    def get(self,request):
        category = Category.objects.all()
        context = {'category':category}
        return render(request,'cms/news/release.html',context=context)
    def post(self,request):
        print('到post这了')
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            print('content',content)
            category_id = form.cleaned_data.get('category')
            category = Category.objects.get(id = category_id)
            print('category_id',category_id)
            thumbnail = form.cleaned_data.get('thumbnail')
            author = request.user
            new = News.objects.create(title=title,content=content,category=category,thumbnail=thumbnail,author=author)
            new.save()
            print('OK')
            return restful.ok()
        print('表单错')
        print('form.get_errors',form.get_errors)
        return restful.params_error(message='G表单问题')
#标签


def category(request):
    if request.method == 'GET':
        categorys = Category.objects.all().order_by("-id")
        content = {'categorys':categorys}
        return render(request,'cms/news/category.html',context=content)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print('name',name)
            category = Category.objects.create(name=name)
            category.save()
            return restful.result(message='添加成功')
        return restful.params_error('表单验证错误')


def image_upload_to_local(request):
    file = request.FILES.get('file')
    file_name = file.name
    with open((os.path.join(settings.CLIENTIMAGE_ROOT,file_name)),'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    url = request.build_absolute_uri(settings.STATIC_URL+'client_image/'+file_name)
    print(url)
    return restful.result(data={'url':url})

def category_modify(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get('id')
        print('category_id',id)
        name = form.cleaned_data.get('name')
        print('category_name',name)
        try:
            Category.objects.filter(pk=id).update(name=name)
            return restful.ok()
        except:
            return restful.params_error('该分类不存在')

    else:
        return restful.params_error(message=form.get_error())


def category_delete(request):
    id = request.POST.get('id')
    print('id',id)
    if id:
        try:
            dele = Category.objects.filter(id=id).delete()
            print('dele',dele)
            return restful.ok()
        except:
            return  restful.params_error(message='数据库无法查到这个ID，请刷新')
    else:
        return restful.params_error(message='没有这个名称，无法删除，请刷新')


def thumbnail_process(request):
    access_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
    secret_key = 'IGhDFYcbCns_3RcEopOwmHLE8M7XctIe_bVwYfHr'
    bucket = 'establish'
    q = qiniuAuth(access_key,secret_key)
    token = q.upload_token(bucket)
    return restful.result(data={'token':token})

def banner_control(request):
    return render(request,'cms/banner/banner.html')


#管理banner
def banner_cms_manager_get(request):
    banner = Banner.objects.all()
    serializer = BannerSerializers(banner,many=True).data
    context = {'banners':serializer}
    return restful.result(data=context)

#添加banner
def banner_cms_manager_add(request):
    form = BannerForm(request.POST)
    if form.is_valid():
        link_to = form.cleaned_data.get('link_to')
        priority = form.cleaned_data.get('priority')
        image_url = form.cleaned_data.get('image_url')
        banner = Banner.objects.create(link_to=link_to,priority=priority,image_url=image_url)
        banner.save()
        return restful.result(data={'banner_id':banner.id})
    else:
        return restful.params_error(form.get_errors())

#删除banner
def banner_cms_manager_delete(request):
    banner_id = request.POST.get('banner_id')
    print('banner_id_POST',banner_id)
    banner_id_get = request.GET.get('banner_id')
    print('banner_id_GET',banner_id_get)
    try:
        banner = Banner.objects.get(id=banner_id).delete()
        return restful.ok()
    except:
        return  restful.params_error(message='没有这条数据,请刷新')


#编辑banner
def banner_cms_manager_edit(request):
    form = BannerForm(request.POST)
    if form.is_valid():
        link_to = form.cleaned_data.get('link_to')
        priority = form.cleaned_data.get('priority')
        image_url = form.cleaned_data.get('image_url')
        banner_id = form.cleaned_data.get('banner_id')
        banner = Banner.objects.filter(id=banner_id)
        banner.update(link_to=link_to,priority=priority,image_url=image_url)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())

#新闻增删改查
def news_cms_manager(request):
    return render(request,'cms/news/news_manager.html')


#慕慕
def lover_mumu(request):
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

    with open('../demo_of_comment.log', 'r') as r:
        try:
            Read = r.readlines()
        except:
            with open('../demo_of_comment.log', 'w') as r:
                Read = r.readlines()

    with open('../demo_of_comment.log', 'w') as w:
        w.write("Time:%s,IP:%s,comment of index click\n" % (str(log_time), ip))
        for i in Read:
            w.write(i)
    return render(request,'cms/banner/mumu.html')