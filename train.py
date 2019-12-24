


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



import httplib2
from urllib.parse import urlencode
import json

ip = '212.156.209.78'
tip = '127.0.0.1'
if str(ip) == tip:
    print('IP相同')
else:
    token = '4120d93d1b807a778e37dd9b37c8d5d8'
    oid = 27558
    mid = 89951
    datatype = 'jsonp'
    callback = 'find'
    headers = {"token": token}
    params = urlencode({'ip': ip, 'datatype': datatype, 'callback': 'find'})
    url = 'http://api.ip138.com/query/?' + params
    http = httplib2.Http()
    response, content = http.request(url, 'GET', headers=headers)
    result = content.decode("utf-8")
    result_extract = result[5:]
    re = result_extract
    num = len(result_extract) - 1
    list = []
    for i in range(num):
        list.append(result_extract[i])
    list = ''.join(list)
    li = json.loads(list)
    ip = li['ip']
    country = li['data'][0]
    province = li['data'][1]
    city = li['data'][2]
    isp = li['data'][3]
    print(list)
    print('城市'+city)