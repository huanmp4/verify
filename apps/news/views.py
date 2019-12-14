from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from apps.news.models import Discover
from apps.news.forms import DiscoverForm
from utils import restful
from apps.register.models import User

# Create your views here.

def index(request):
    return render(request,'news/index.html')

class Discover_Process(View):
    def get(self,request):
        discover = Discover.objects.all()
        context = {'discover':discover}
        return render(request,'news/discover.html',context)

    def post(self,request):
        form = DiscoverForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            if str(request.user) != 'AnonymousUser':
                author = request.user
            else:
                author = User.objects.get(uid = 123123)
            print('最终形态',author)
            print('content',content)
            disc = Discover.objects.create(content=content,author = author)
            disc.save()
            return restful.ok()
        else:
            return restful.params_error('内容或标题不能为空')