from django.http import JsonResponse
from apps.cms.models import Address
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


def get_address(request,content='主页留言'):
    content = content
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    dd = request.META
    if http_x_forwarded_for:
        ip = http_x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    if str(ip) == '127.0.0.1':
        pass
    else:
        ip = ip
        r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
        print('r.json()',r.json()['code'] )
        if r.json()['code'] == 0:
            i = r.json()['data']
            country = i['country']  # 国家
            area = i['area']  # 区域
            region = i['region']  # 地区
            city = i['city']  # 城市
            isp = i['isp']  # 运营商

            print('国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, area, region, city, isp))
            address = Address.objects.create(ip=ip, content=content, country=country, province=region, city=city, isp=isp)
            address.save()
        else:
            print("错误! ip: %s" % ip)
        return ip
