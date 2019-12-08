from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import NewsForm
from ..news.models import News
from utils import restful
from .forms import CategoryForm
from apps.news.models import Category
import os
from django.conf import settings
from qiniu import Auth as qiniuAuth
# Create your views here.
def home(request):
    return render(request,'cms/home.html')


def news_release(request):
    return render(request,'cms/news/release.html')

def ReleaseNews(request):
    if request.POST:
        form = NewsForm(request.POST)
        print('到这里了')
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print('name',name)
            content = form.cleaned_data.get('content')
            news=News.objects.create(name=name,content=content)
            news.save()
            print('成功')
            return restful.ok()
        else:
            return restful.params_error(form.get_errors())
    else:
        return render(request,'cms/news/release.html')

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
    secret_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
    bucket = 'establish'
    q = qiniuAuth(access_key,secret_key)
    token = q.upload_token(bucket)
    return restful.result(data={'token':token})