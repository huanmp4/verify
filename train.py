


a = {'password': [{'message': '密码长度不能少于4位', 'code': 'min_length'}]}

b = {}
for key,value in a.items():
    register = []
    for var in value:
        register.append(var['message'])
    b[key] = register[0]



#最大数为100
chance = min(100,max(10,int(9)))


import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=True)
aa=mc.get('13005611192')


from qiniu import Auth

access_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
secret_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'

Q = Auth(access_key,secret_key)

import os
from qiniu import Auth, put_file, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
secret_key = 'IGhDFYcbCns_3RcEopOwmHLE8M7XctIe_bVwYfHr'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'establish'
#上传后保存的文件名
key = 'chicken.png'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径

#
import requests
# from datetime import datetime
# time = datetime.now()
# ip = '180.97.118.223'
# r=requests.get(url='http://ip.taobao.com/service/getIpInfo.php', params=ip,timeout=3)
# ping = r.json()
# print(ping)
# i = r.json()['data']
# country = i['country']  # 国家
# area = i['area']  # 区域
# region = i['region']  # 地区
# city = i['city']  # 城市
# isp = i['isp']  # 运营商
# print('国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' % (country, area, region, city, isp))
#

import httplib2
from urllib.parse import urlencode #python3
#from urllib import urlencode #python2
import json
ip = '14.210.1.180'
token='4120d93d1b807a778e37dd9b37c8d5d8'
oid=27558
mid=89951
datatype='jsonp'
callback='find'
headers = {"token":token}
params = urlencode({'ip':ip,'datatype':datatype,'callback':'find'})
url = 'http://api.ip138.com/query/?'+params
http = httplib2.Http()
response, content = http.request(url,'GET',headers=headers)
result=content.decode("utf-8")

result_extract = result[5:]
re = result_extract
num = len(result_extract) - 1
list = []
for i in range(num):
    list.append(result_extract[i])
list=''.join(list)
li = json.loads(list)
ip = li['ip']
country = li['data'][0]
province = li['data'][1]
city = li['data'][2]
isp = li[da]
print(li)
