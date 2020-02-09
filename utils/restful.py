from django.http import JsonResponse
from apps.cms.models import Address
import httplib2
from urllib.parse import urlencode
import json


import requests,time

class HttpCode(object):
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500
    formerror = 300
    passworderror = 301
    accounterror = 302
    sendmessageerror = 311


def result(code=HttpCode.ok,message=None,data=None):
    json_dict = {'code':code,'message':message,'data':data}
    return JsonResponse(json_dict)

def params_error(message=None,data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)

def auth_error(message=None,data=None):
    return result(code=HttpCode.unauth,message=message,data=data)

def password_error(message='密码错误',data=None):
    return result(code=HttpCode.passworderror,message=message,data=data)

def account_error(message='帐号不存在',data=None):

    return result(code=HttpCode.accounterror,message=message,data=data)

def method_error(message=None,data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)

def server_error(message=None,data=None):
    return result(code=HttpCode.servererror,message=message,data=data)

def form_error(message=None,data=None):
    return result(code=HttpCode.formerror,message=message,data=data)

def ok():
    return result()


class FormError(object):
    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()  # {'password': [{'message': '密码长度不能少于4位', 'code': 'min_length'}]}
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return '表单无验证无数据'


def get_address_by_138ip(request,content='主页留言'):
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_x_forwarded_for:
        ip_addr = http_x_forwarded_for.split(',')[0]
        #斯洛文尼亚
        invalid_save_address_by_138ip(ip = ip_addr,contentype =content)
        #当前IP
    else:
        ip_addr2 = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        #法西兰
        invalid_save_address_by_138ip(ip=ip_addr2, contentype=content)
        # address = Address.objects.create(ip=ip_addr2, content=content)
        # address.save()
        #本机IP
#save ip



#
#
# #有效保存IP地址
# def save_address_by_138ip(ip,contentype):
#     token = '4120d93d1b807a778e37dd9b37c8d5d8'
#     oid = 27558
#     mid = 89951
#     datatype = 'jsonp'
#     callback = 'find'
#     headers = {"token": token}
#     params = urlencode({'ip': ip, 'datatype': datatype, 'callback': 'find'})
#     url = 'http://api.ip138.com/query/?' + params
#     http = httplib2.Http()
#     response, content = http.request(url, 'GET', headers=headers)
#     result = content.decode("utf-8")
#     result_extract = result[5:]
#     re = result_extract
#     num = len(result_extract) - 1
#     list = []
#     for i in range(num):
#         list.append(result_extract[i])
#     list = ''.join(list)
#     li = json.loads(list)
#     ip = li['ip']
#     country = li['data'][0]
#     province = li['data'][1]
#     city = li['data'][2]
#     isp = li['data'][3]
#     try:
#         address = Address.objects.create(ip=ip, content=contentype, country=country, province=province, city=city, isp=isp)
#         address.save()
#     except:
#         pass



#当IP地址无效时：
def invalid_save_address_by_138ip(ip,contentype):
    ip = ip or '无'
    print('ip:',ip)
    try:
        address = Address.objects.create(ip=ip, content=contentype, country='无', province='无', city='无', isp='无')
        address.save()
    except:
        pass