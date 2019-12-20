

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



from datetime import datetime
time = datetime.now()
print('time',time)


# from django import template
# from datetime import datetime
# from django.utils.timezone import now as now_func,localtime
#
# register = template.Library()
# now1 = now_func()
# print(now1)

import re
pattern = "[\u4e00-\u9fa5]+|"
string = '在要要111dd'
result = re.findall(pattern, string)
print('正则',result)
