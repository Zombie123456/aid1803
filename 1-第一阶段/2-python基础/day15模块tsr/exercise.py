
# import time
# 电子时钟
# def show_time():
    # while True:
    #     t=time.localtime()
    #     print('\r %02d:%02d:%02d' % t[3:6],
    #         end='')
    #     time.sleep(1)
# show_time()

# 生日
# import time
# y=int(input('输入出生年:'))
# m=int(input('输入出生月:'))
# d=int(input('输入出生日:'))
# t=time.mktime((y,m,d,0,0,0,0,0,0))
# time_tuple=time.localtime(t)
# week=time_tuple[6]
# l=['星期一','星期二','星期三','星期四',
#    '星期五','星期六','星期日']
# print(l[week])
# t=time.time()-t
# d=t/(60*60*24)
# print('出生已',d,'天')

# 生成6位随机密码
# import random
# l='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_0123456789'
# s=''
# for i in range(6):
#     s+=random.choice(l)
# print(s)

# 练习:
#   1.编写一个闹钟程序,启动时设置定时时间:(小时和分钟)
#   到时间后打印'时间到....'然后退出
# import time
# def clock():
#     a=int(input('请输入闹铃时间(小时):'))
#     b=int(input('请输入闹铃时间(分钟):'))
#     while True:
#         t=time.localtime()
#         print('\r %02d:%02d:%02d' % t[3:6],
#             end='')
#         time.sleep(1)
#         if t[3:5]==(a,b):
#             print('时间到',a,'时',b,'分',end='')
# clock()

#   2.模拟斗地主发牌,扑克牌共54张:花色:黑桃('\u2660'),
#   梅花('\u2663'),方块('\u2665'),红桃('\u2666')
#   数值:A2-10JQK,大小王,三个人,一人17张,底牌留3张:
#   输入回车,打印第一人的17张牌
#   输入回车,打印第二人的17张牌
#   输入回车,打印第三人的17张牌
#   再回车,打印三张底牌
# 斗地主fight the landlord
# import random as r
# def ftl_deal():
#     l=['A','2','3','4','5','6','7','8',
#    '9','10','J','Q','K']
#     l1=['JOKER','joker']
#     l1.extend(map(lambda x:x+'\u2660',l))
#     l1.extend(map(lambda x:x+'\u2663',l))
#     l1.extend(map(lambda x:x+'\u2665',l))
#     l1.extend(map(lambda x:x+'\u2666',l))
#     r.shuffle(l1)
#     input('输入回车显示第一人牌')
#     print('第一人牌:',l1[0:17])
#     input('输入回车显示第二人牌')
#     print('第二人牌:',l1[17:34])
#     input('输入回车显示第三人牌')
#     print('第三人牌:',l1[34:51])
#     input('输入回车显示底牌')
#     print('底牌:',l1[51:])
# ftl_deal()
















