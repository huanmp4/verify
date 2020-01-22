from django.shortcuts import render
from .models import Party
from utils import restful


def index(request):
    party = Party.objects.all()
    count = party.count()
    return  render(request,'party/index.html',{'partys':party,'count':count})

def comment(request):
    return render(request,'party/comment.html')

def write(request):
    name = request.GET.get('name')
    memo = request.GET.get('memo')
    cellphone = request.GET.get('cellphone')
    print('name',name)

    exists=Party.objects.filter(name=name).exists()
    if exists:
        return restful.result(code=400,message='姓名已存在')
    else:
        party = Party.objects.create(name=name,memo=memo,cellphone=cellphone)
        return restful.ok()

def delete(request):
    print('到这了')
    id = request.GET.get('id')
    Party.objects.get(pk=id).delete()
    return restful.ok()