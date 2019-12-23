#
#
#
#
#
#
#
# num_sixbit = []
# for i in range(4):
#     num_sixbit += random.choices(num)
# print(num_sixbit)
#
# num_sixbit.reverse()
# digit = ''
# sim = ''.join(num_sixbit)
#
# num1 = '%s%s%s%s'%(num_sixbit[0],num_sixbit[1],num_sixbit[2],num_sixbit[3])
# print(num1)
#
#
#
# sword = {'物理攻击':'14','魔法攻击':'26','道术攻击':'15'}
# wand = {'物理攻击':'32','魔法攻击':'11','道术攻击':'20'}
# #
#
# dic=dict(map(sword,wand))
# print(dic)

#
#
# integer = [11,22,23,44,3,1]
# print(integer)
# integer2 = tuple(integer)
# print(integer2)
# result = sum(integer2)
# print(result)
#
#
# price = [50,110,250]
# newprice = []
# number=len(price)
# for i in range(number):
#     sword2=price[i]*0.5
#     newprice.append(s)
#
# print(newprice)
#
#
# # price2 = [int(0.5*x) for x in price]
# # print(price2)
# price = [50, 110, 250, 11, 22, 23, 44, 3, 1]
#
# newprice = [x for x in price if x > 4]
#
#
# import random
# newdigit = [random.randint(10,100)for x in range(10)]
#
#
#
# room = []
#
#
# temporary = []
# temporary2 = []
# for i in range(1101,1111):
#     temporary.append(i)
# room.append(temporary)
#
#
# for i in range(2101,2111):
#     temporary2.append(i)
# room.append(temporary2)
#
#
#
# verse = []
# digit = -1
# temporary_one = [[],[],[],[],[]]
# for i in range(4):
#     for j in range(5):
#         digit += 1
#         if digit > 4:
#             digit = 0
#         temp = metho[i][j]
#         temporary_one[digit].insert(0,temp)
#
#
#
#
# str1 = "千山鸟飞绝"
# str2 = "万径人踪灭"
# str3 = "孤舟蓑笠翁"
# str4 = "独钓寒江雪"
# #
# #
#
# #
#
# register = [tuple(str1),tuple(str2),tuple(str3),tuple(str4)]
#
# register.sort(reverse = True)
#
#
# for i in range(5):
#     for j in range(4):
#         if j == 0:
#             print('\t\t',end = '')
#         if j == 3:
#             print(register[j][i])
#         else:
#             print(register[j][i],end = '')
#
#
# register.sort(reverse = False)
# for i in range(4):
#     for j in range(5):
#         if j == 4:
#             print(register[i][j])
#         else:
#             print(register[i][j],end = '')
#
#
#
#
#
#

coffeename = ['蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚','拿铁']
print('欢迎光临!!!\n本店有以下几种咖啡供您选择:')
for coffee in coffeename:
   print(coffee+'咖啡',end = ''+' ')

team = {"火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼"}
if '雷霆' in team:team.remove('森林狼')

#
authoriza = {i:j for i,j in zip(team,coffeename)}
print(authoriza)
#
# authorization = [value for key,value in authoriza.items() ]
#
# print(authorization)
#
#
#
# # traceback = dict(zip(team,coffeename))
# #
# # for j,k in traceback.items():
# #     print(j+'喜欢喝的咖啡是:'+k)
# #
# # print(traceback)
#
#
#
#
# # dd=coffeename.remove('摩卡')
# period = {i:j for i,j in zip(team,coffeename)}
# print(period)
# regularly = [value for key,value in period.items()]
# print(regularly) #定期
#
# for index,i in enumerate(regularly):
#     if index % 2 == 1:
#         print(i)
#     else:
#         print(i+'1',end = '')
#
#
#
# #
# # num = []
# # for i in range(10):
# #     num.append(i)
# # word = dict(zip(team,coffeename))
# # print(word)
# #
# # invoice = dict.fromkeys(team)
# # print(invoice)
# #
# # number = dict.fromkeys(num)
# # print(number)
# #
# #
# # print(num)
#
#
# team = ["火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼"]
# coffeename = ['蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚','拿铁']
# # import random
# # #
# # # column = [random.randint(1,10) for i in range(5)]
# # # print(column)
# # #
# # # virtual = {'这是'+i+'喜欢':j+'咖啡' for i,j in zip(team,coffeename)}
# # # print(virtual)
#
# # print('==篮球战队==')
# # for index,j in enumerate(team):
# #     if index == 3:
# #         print(j)
# #     if index == 6:
# #         print(j)
# #     else:
# #         print(j+'\t',end = '')
#
# # prompt = ['车次','目的地\t','开车','到达','历时']
# # T40 = ['T40\t','长春-北京','00:12','12:20','25:08']
# # G1940 = ['G1940','长春-广州','00:12','12:20','25:08']
# # world = [list(prompt),list(T40),list(G1940)]
# # for i in range(3):
# #     for j in range(5):
# #         if j == 4:
# #             print(world[i][j])
# #         else:
# #             print(world[i][j]+'\t\t', end='')
# #
# # train = T40
# # name =('吴嫔嫔','陈志华')
# # nameconfirm = [ x for x in name]
# # print('您选择的车次是:%s,乘车人是:%s,火车是: %s出发,请作好准备'%(train[0],name,train[2]))
# #
# # #
# team = ["火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼"]
# enumerate1 =(6,1.3,5,22,14,2,10,7)
# enumerate = {i:j for i,j in zip(team,enumerate1)}
#
# investigate = sorted(enumerate.items(),key = lambda enumerate:enumerate[1])
# print(investigate)
# # print(newteam)
# # print(newlink)
# # iterable = {i:j for i,j in newlink}
# print(iterable)
# print('==排名由上至下==')
# import datetime
# date = datetime.datetime.now()
# print(date)
# import re
# interpreter = open('D:\\synbol\\breakout_one.txt','r')
# during=interpreter.read()
# import re
# terrible = '192.168.1.87 dddf33332222'
# terrible2 = '56789'
# pattern = '[\u4e00-\u9fa5]+'
# pattern2 = '\W'
# pattern3 = '[^\u4e00-\u9fa5]|\W'
# string = 'stru\w{5}'
# pattern4 = r'(13[4-9]{8})'
# pattern5 = '([0-9]{1,3}(\.[0-9]{1,3}){3})'
# match = re.findall(pattern5,terrible)
# print(match)
# such = 0
# font = '方正黑体蓝色'
# for i in match:
#     if i == font:
# #         continue
# #     elif i == '方正黑体简体':
# #         continue
# #     else:
# #         such += 1
# #         print(i, end=',')
# #         if such == 10:
# #             print(i)
# #             such = 0
#
# # import re
# # field = r'Trojan|黑客'
# # about = '我是一个程序员，喜欢Trojan'
# # about2 = '我是一个程序员，喜欢网络开发'
# #
# # search = re.sub(field,'**',about)
# # print(search)
#
# # import random
# # import re
# # same = 50
# # same2 = 5
# #
# # scratch = str(same)
# # temporary = '[0-9]{1,2}|[1-9]{1,2}'
# # group = re.search(temporary,scratch)
# # if group == None:
# #     print('输入的数字有误!')
# # else:
# #     print(group)
# #
#
# #[int(x) for x in goup]
# #
# # def rob(red_bag,digit):
# #     amount = red_bag
# #     number = digit
# #     money = []
# #     if number >= 2:
# #         temp=amount / 2
# #         first = random.randint(1,temp)
# #         money.append(first)
# #         for i in range(number-1):
# #             terminal = amount - first
# #             second = random.randint(1,terminal)
# #             money.append(second)
# #     else:
# #         money.append(amount)
# #     print(money)
# #
# #
# # rob(same,same2)
#
# # import re
# #
# # virtualvenv = '@明 日 , 科 技 @什 么 鬼 @好吧'
# # environment = r'@'
# # bear = '[^\s|,]'
# # environment3 = re.findall(bear,virtualvenv)
# #
# # print(environment3)
# # del environment3[0]
# # pattern = ''.join(environment3)
# # print(pattern)
# #
# #
# # environment1 = re.split(environment,pattern)
# # print(environment1)
# #
# #
# # word = '地要要械banana is a good fruit,go人员123,gdo'
# # pattern = '[a-zA-Z]|\s|\d'
# # pattern2 = 'g+'
# # optimization = re.findall(pattern2,word)
# # print(optimization)
# # optimization = ''.join(optimization)
# #
# #
# # def submit(content):
# #
# #     import re
# #     behaviour = '草你妈|变态|垃圾'
# #     evolution = re.sub(behaviour,'**',content)
# #     print(evolution)
# # submit('你这个死变态，草你妈的，你是不是垃圾')
# #
# #
# # def person(*person):
# #
# #
# #     for i in person:
# #         name = i[0]
# #         weight = i[1]
# #         height = i[2]
# #         BMI = weight/(height*height)
# #         print('='*20)
# #         print('%s,您的体重：%s斤,身高：%s米\n你的BMI值:%s'%(name,weight,height,BMI))
# #         print(name + '你的体重:'+str(weight))
# #         if BMI <= 18.5:
# #             print('瘦皮猴')
# #         if BMI > 18.5 and BMI <=24.9:
# #             print('死肥宅')
# #         if BMI > 24.9 and BMI <=29.5:
# #             print('体重还行')
# #         if BMI > 29.5:
# #             print('死肥宅')
# #         print('='*20)
# #
# # list_j = ('寿寿',140,172)
# # list_ss = ('进哥',130,165)
# # list_jg = ('江泽平',160,175)
# # person(list_j,list_ss)
# #
# #
# #
# # def constellation(**sign):
# #     print(sign)
# #     for key,value in sign.items():
# #         print('['+key+']的星座是:'+value)
# # star = {'宾宾':'处女座'}
# # constellation(寿寿='处女座',进 = '还钱座')
# # constellation(**star)
#
# # def evolution(amount):
# #     i = sum(amount)
# #     newamount = 0
# #     if i <200:
# #         newamount = amount
# #     elif 200 >= i <400:
# #         newamount = amount * 0.9
# #     return newamount
# # money=evolution(220)
# # print(money)
#
#
# import math
#
# r = 12
# result = lambda r:math.pi*r/2
# print(result(r))
#
#
# bookinfo = [('不一样的卡梅拉（全套)',22.50,120),('零基础学Android',65.10,89.80),
#         ('摆渡人',23.40,36.00),('福尔摩斯探案全集8册',22.50,128)]
# evacuate = sorted(bookinfo,key = lambda bookinfo:(bookinfo[1]/bookinfo[2]))
# print(evacuate)
#
# book_discount = []
# book_num = len(bookinfo)
# book_division =[]
# quality = []
# quality2 = []
# for i in range(book_num):
#     book_discount.append([])
#     book_discount[i].append(evacuate[i][0])
#     division=round((evacuate[i][1]/evacuate[i][2]),2)
#     book_discount[i].append(division)
#     quality.append(evacuate[i][0])
#     quality2.append(division)
# print(book_discount)
#
# resentment = {i:j for i,j in zip(quality,quality2)}
#
# for key,value in resentment.items():
#     print('产品:'+key+'：%.1f折'%(value*10))
#
# yuan = 500
# # dollar = [yuan*6.28]
#
# class Goose:
#     count = 0
#     beak = '我有啄，可以啄虫子吃'
#     wing = '我有翅膀,可以飞'
#     claw = '我有利爪'
#     flight = '飞啊飞啊，飞起来'
#     def __init__(self):
#         print(Goose.beak)
#         Goose.fly(self)
#     def fly(self):
#         if Goose.count == 100:
#             continue
#             break
#         else:
#
#             Goose.count += 1
#             print(Goose.count)
#             Goose()
#
#
# Goose()
# beak = '我有啄，可以啄虫子吃'
#
#
#
#
# class depand:
#     wing = '什么鬼'
#     def __init__(self):
#         print('init_one')
#     def _primary(self):
#         depand.__init__(self)
#
# primary = depand()
# primary._primary()
#
#
# class TvWatch:
#     watch_list = ['复联3','奇异博士','超人2']
#     defoult = '超人1'
#     xx = '什么鬼，没选择'
#
#     def __init__(self,play):
#         self._play = play
#         self.chase = ['超人5']
#     @property
#     def Show(self):
#         return self._play
#     def already_pay(self):
#         for x in self.chase:
#             print(x,end = ' ')
#     def check(self):
#         return self.chase
#     def Repay(self,value):
#         if value in TvWatch.watch_list:
#             self.chase.append(value)
#             return '您已重新购买《%s》电影'%value
#         else:
#             return '不好意思，您所购买的电影已下架，请重新选择'
#
# primary=TvWatch('男人帮')
# xx=primary.Repay('复联3')
# print(xx)
#
# print('你已购买：')
# primary.already_pay()
#
# class Fruit:
#     girl = '建宁公主'
#     girl_empty = ''
#     def date(self):
#         print('我之前的爱人是%s'%Fruit.girl)
#         print('现在找了个新欢:%s,她是最美的'%Fruit.girl_empty)
#         print('balabala')
#
#
# class Servaral(Fruit):
#     girl = '西施'
#     def __init__(self):
#         print('我是韩子欢')
#         Fruit.girl_empty = '貂蝉'
#
#
#
#
#
# from random import random,uniform,randrange,choice,sample
# simulation=random()
# recipes = round(uniform(1.11,10.99),2)
# basic = [randrange(2,10,5) for i in range(10)]
# custom = sample(['我','想','努力'],k = 2)
# print(custom)
#
# class abstraction:
#     color = '<orange>'
#     def recipes(self,xx):
#         print('hallo every one! I\'m  %s color \nI\'m change from now I silver\mthrank you' %xx)
#
# class simulation(abstraction):
#     color = '<green>'
#     def __init__(self,abstraction):
#         print('productive')
#         print('My color is:'+abstraction)
#
# golden = simulation('grey')
# golden.recipes('golden')
#
