from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from utils import restful
from .forms import CategoryForm,NewsForm,BannerForm
from apps.news.models import Category,Banner,News,Discover
import os,time
from django.conf import settings
from qiniu import Auth as qiniuAuth
from apps.news.serializers import BannerSerializers
from apps.news.forms import DiscoverForm
from apps.register.models import User
from .models import Address
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.paginator import Paginator
from urllib import parse

#权限访问装饰器
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home(request):
    return render(request, 'cms/news/home.html')


@staff_member_required(login_url='index')
def news_release(request):
    return render(request,'cms/news/release.html')


@method_decorator(permission_required(perm='news.add_news',login_url='/'),name='dispatch')
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
        categorys = Category.objects.prefetch_related('news_set').all().order_by("-id")
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

@method_decorator(permission_required(perm='category.change_category',login_url='/'),name='dispatch')
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

@method_decorator(permission_required(perm='category.delete_category',login_url='/'),name='dispatch')
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
@method_decorator(permission_required(perm='banner.add_banner',login_url='/'),name='dispatch')
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



#慕慕
def lover_mumu(request):
    restful.get_address_by_138ip(request,'慕慕blog访问')
    return render(request,'cms/banner/mumu.html')


#主页留言版
def Discover_Process(request):
    count = settings.PAGE_LOAD_NUM
    if request.method == 'GET':
        pp = restful.get_address_by_138ip(request=request)
        print(pp)
        discover = Discover.objects.all().select_related('author')
        context = {'discover': discover}
        return render(request, 'news/discover.html', context)
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
                    author = User.objects.create_user(username='还未注册用户1', password=12341234, telephone=13005611199,
                                                      is_staff=0)
            disc = Discover.objects.create(content=content, author=author)
            disc.save()
            return restful.ok()
        else:
            return restful.params_error('内容或标题不能为空')

#渲染IP页面
def demo_cms_address_ip(request):
    address = Address.objects.all()
    return render(request,'cms/demo/address.html',context={'addresses':address})


#查用户
def demo_cms_manager_client(request):
    user = User.objects.all()
    return render(request,'cms/demo/user_manager.html',context={'users':user})

#删除IP
def demo_cms_delete_ip(request):
    pk = request.POST.get('pk')
    try:
        Address.objects.get(pk=pk).delete()
        return restful.ok()
    except :
        return restful.params_error('未查到该id')

#新闻列表遍历
class News_preview_cms_all(View):
    def get(self,request):
        start = request.GET.get('start')
        end = request.GET.get('end')
        category = int(request.GET.get('category',0) or 0)
        title = request.GET.get('news-title')
        content = request.GET.get('news-content')
        p_for_web = request.GET.get('p_for_web',1)
        print('start',start)
        print('end',end)
        print('title', title)
        print('content', content)
        print('category', category)

        newses = News.objects.select_related('category','author').all()

        if start or end:
            if start:
                try :
                    start = make_aware(datetime.strptime(start, '%Y/%m/%d'))
                    print('start', start)
                except ValueError :
                    start = start
            else:
                start = datetime(year=2019, month=5, day=1)
                print('start', start)
            if end:
                try:
                    end = make_aware(datetime.strptime(end, '%Y/%m/%d'))
                except ValueError :
                    end = end
            else:
                end = datetime.now()
                print('end', end)
            newses = newses.filter(pub_time__range=(start, end))
        if category:
            newses = newses.filter(category=category)
        if title:
            newses = newses.filter(title__icontains=title)
        if content:
            newses = newses.filter(content__icontains=content)

        #&start=20121111&start=20121112
        urlencode = '&' + parse.urlencode({'start': start or '',
                                           'end': end or '',
                                           'category': category or '',
                                           'news-title': title or '',
                                           'news-content': content or ''
                                           })
        context = self.get_page(newses=newses,p_for_web=p_for_web)
        # 加上额外的过滤
        urlencode = {'urlencode': urlencode,}
        context.update(urlencode)
        return render(request,'cms/news/news_preview.html',context=context)

    def get_page(self,newses,p_for_web):
        p = Paginator(newses, 6)
        page_current = p.page(p_for_web)
        print('')
        page_range = p.page_range
        page_hasPrevious = page_current.has_previous()
        page_hasNext = page_current.has_next()
        print('p.page_range', p.page_range)
        print('p.page(1)', p.page(p_for_web))
        categorys = Category.objects.all()
        # urlencode就相当于在每个字典前加个‘&’
        # 如category=2&news_title='他'&news-content='我
        # 计算出前面页数
        current = page_current.number
        # 计算出共有几页
        score = p.num_pages
        arround_range = 2


        left_has_more = False
        right_has_more = False
        # 如果当前页数小于或等于4，那就range,且不显示小...
        if current <= arround_range + 1:
            left_point = range(1, current)
        else:
            left_has_more = True
            # 如果前当页数大于等于4，左边当前页数-2，range面前页数,并显示小点点
            left_point = range(current - arround_range, current)
        # 如果前面页数 大于等于 所有的页数
        if current >= score - arround_range - 1:
            right_point = range(current , score + 1)
        else:
            right_point = range(current , current + arround_range + 1)

        context = {
            # 新闻列表
            'newses': page_current.object_list,
            # 当前获取页码的页面
            'page_current': page_current,
            # 当前页码的range
            'page_range': page_range,
            # 有上一页吗
            'page_hasPrevious': page_hasPrevious,
            # 有下一页吗
            'page_hasNext': page_hasNext,
            'categorys': categorys,
            # 当前第几页
            'page_current_previous': page_current.number,
            # 共有几页
            'pagenums': p.num_pages,
            'left_points': left_point,
            'right_points': right_point,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }
        return context



#新闻编辑
def news_preview_cms_edit(request):
    news_id = request.GET.get('news_id')
    news = News.objects.select_related('category').get(pk = news_id)
    category = Category.objects.all()
    return render(request,'cms/news/release.html',{'news':news,'category':category})

#新闻删除
def news_preview_cms_delete(request):
    news_id = request.POST.get('news_id')
    print('news_id',news_id)
    News.objects.get(id=news_id).delete()
    return restful.ok()