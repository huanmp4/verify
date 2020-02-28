from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from apps.register.models import User
from apps.register.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponse
from apps.register.decorators import superuser_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from utils import restful
@superuser_required
def staff(request):
    staff = User.objects.all()
    context ={'staffs':staff}
    return render(request,'cms/staff/staff.html',context)

@method_decorator(superuser_required,name='dispatch')
class StaffAdd(View):
    def get(self,request):
        groups = Group.objects.all()
        return render(request,'cms/staff/addstaff.html',{'groups':groups})
    def post(self,request):
        username = request.POST.get('username')
        print('username',username)
        if username:
            group_id = request.POST.getlist('groups')
            for group in group_id:
                print('groupid：' + group)
            user = User.objects.get(username=username)
            print('user:',user.username)
            group = Group.objects.filter(id__in=group_id)
            user.groups.set(group)
            user.save()
            return redirect(reverse('cms:staff'))
        else:
            messages.info(message='用户名不存在',request=request)
            return HttpResponse('用户名不存在')