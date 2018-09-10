#!/usr/bin/python3
# 练习:
#   输入一个正整数判断是奇数还是偶数打印结果
# a=int(input('请输入一个正整数:'))
# if a//2 == 0:
#     print(a,'是偶数')
# else:
#     print(a,'是奇数')

# 练习:
#   1.输入一个季度1-4,输出这个季度有哪几个月,
#   如果输入不是整数,则提示用户输错了
# season=int(input('请输入季度(1-4):'))
# if   season == 1:
#     print('是1,2,3月')
# elif season == 2:
#     print('是4,5,6月')
# elif season == 3:
#     print('是7,8,9月')
# elif season == 4:
#     print('是10,11,12月')
# else:
#     print('用户您输错了')

#   2.输入一年中的月份(1-12),输出这个月在哪个季度,
#   如果输入的是其他数,则提示你输入错误
# month=int(input('请输入月份(1-12):'))
# if   0 < month < 4:
#     print('是一季度')
# elif 3 < month
#     print('是二季度')
# elif 6 < month < 10:
#     print('是三季度')
# elif 9 < month < 13:
#     print('是四季度')
# else :print('用户您输错了')

# 商场促销,满100减20
# money=int(input('请输入商品金额'))
# pay=money-20 if money >= 100 else money
# print('您需要支付:{}元'.format(pay))

# 练习:
# 1.写一个程序,输入一个数,用if语句计算并打印这个数的绝对值
# (不能使用abs函数)
# a=int(input('请输入一个数'))
# if a >= 0:
#     print('数为',a)
# else :
#     print('数为',-a)

# 2.写一个程序,输入一个数,用条件表达式计算并打印这个数的绝对值
# a=int(input('请输入一个数'))
# b=a if a >= 0 else -a
# print('数为',b)

# 练习:
#   1.北京出租车计价器:
#     收费标准:
#       3公里内13元
#       超出3公里,每公里2.3元/公里
#       空驶费:超过15公里后,每公里加收1.15元空驶费
#     要求:
#       输出公里数,打印出费用金额(以元为单位4舍五入)
# km=int(input('请输入当前行驶里程:'))
# money=13
# if 3<km:
#     money+=(km-3)*2.3
# if km>15 :  
#     money+=(km-15)*1.15
# print('花费{}元'.format(round(money)))

#   2.输入一个学生的三科成绩:
#     1)打印出最高分是多少分
#     2)打印出最低分是多少分
# a=int(input('请输入第一科成绩:'))
# b=int(input('请输入第二科成绩:'))
# c=int(input('请输入第三科成绩:'))
#  #法1:
# ma=a
# if ma<b:
#     ma=b
# if ma<c:
#     ma=c
#  #法二
# d=[a,b,c]
# print('最高分是{}分'.format(max(d)))
# print('最低分是{}分'.format(min(d)))

#   3.给出一个年份,判断是否为闰年并打印
# year=int(input('给出一个年份:'))
 #法一
# if year%4==0 and year%100!=0 or year%400==0:
#     print('是闰年')
# else:
#     print('不是闰年')
#  #法二
# if year%400==0:
#     print('是闰年')
# elif year%100==0:
#     print('不是闰年')
# elif year%4==0:
#     print('是闰年')
# else :
#     print('不是闰年')

#   4.BMI指数
#     BMI=体重(公斤)/身高的平方(米)
#     18.5-24正常
#     输入身高和体重,打印BMI值并打印体重状态
# weight=int(input('请输入您的体重(kg):'))
# height=float(input('请输入您的身高(m):'))
# BMI=weight/height**2
# print('BMI指数为:',BMI)
# if BMI<18.5:
#     print('体重过轻')
# if 18.5<=BMI<=24:
#     print('体重正常')
# if BMI>24:
#     print('体重过重')
