from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import NewsForm
from ..news.models import News
from utils import restful
from .forms import CategoryForm
from apps.news.models import Category

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
        categorys = Category.objects.all()
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
    with open(file.name,'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return restful.ok()