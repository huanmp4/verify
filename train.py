

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

from qiniu import Auth

access_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
secret_key = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'

Q = Auth(access_key,secret_key)
print(Q)