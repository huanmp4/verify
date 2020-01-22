


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




import hmac,os
import time,datetime
import hashlib
UserKey = 'c982d508182a4fb6'
UserKey = UserKey.encode('utf-8')
userid = '9b594b02a300443eb23fdb723ef74f68'
mediald = 'http://jmrcwcw03u4rd6ptgzj.exp.bcevod.com/mda-jmssk05f5a834fdh/mda-jmssk05f5a834fdh.m3u8'
extension = os.path.splitext(mediald)[1]
mediald = mediald.split('/')[-1].replace('.m3u8','')
expiration = int(time.time())+(60*60*2)
media_and_time = '/{0}/{1}'.format(mediald,expiration).encode('utf-8')
signature = hmac.new(UserKey,media_and_time,digestmod=hashlib.sha256).hexdigest()
token = '{0}_{1}_{2}'.format(signature,userid,expiration)
print('signature',signature)
print('mediald',mediald)
print('extension',extension)
print('media_and_time',media_and_time)
print('token',token)
