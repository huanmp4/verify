from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from ..news.models import News
from utils import restful
from .forms import CategoryForm,NewsForm
from apps.news.models import Category
import os
from django.conf import settings
from qiniu import Auth as qiniuAuth
# Create your views here.
def home(request):
    return render(request,'cms/home.html')


def news_release(request):
    return render(request,'cms/news/release.html')

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


def category_thumbnail(request):
    file = request.FILES.get('file')

    with open((os.path.join(settings.CLIENTIMAGE_ROOT,file.name)),'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    print(os.path.join(settings.CLIENTIMAGE_ROOT+file.name))
    return restful.ok()

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