

a = {'password': [{'message': '密码长度不能少于4位', 'code': 'min_length'}]}

b = {}
for key,value in a.items():
    register = []
    for var in value:
        register.append(var['message'])
    b[key] = register[0]



#最大数为100
chance = min(100,max(10,int(9)))
print(chance)

import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=True)
aa=mc.get('13005611192')
print(aa)