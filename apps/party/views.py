from django.shortcuts import render
from .models import Party
from utils import restful
from django.views import View
from .serializers import PartySerializers

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

class Edit(View):
    def get(self,request):
        id = request.GET.get('id')
        print('get到这了',id)
        party = Party.objects.get(pk=id)
        party2 = PartySerializers(party).data
        return restful.result(data={'party':party2})
    def post(self,request):
        id = request.POST.get('id')
        cellphone = request.POST.get('cellphone')
        name = request.POST.get('name'or'')
        memo = request.POST.get('memo'or'')
        money = request.POST.get('money'or'')

        print('POST,id到了！！！！！', id)
        print('cellphone', cellphone)
        print('name', name)
        print('memo', memo)
        print('money', money)
        party = Party.objects.filter(pk = id)
        party.update(cellphone=cellphone,name=name,memo=memo,money=money)

        return restful.ok()
