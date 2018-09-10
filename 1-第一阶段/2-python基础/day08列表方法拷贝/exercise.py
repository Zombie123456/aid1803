# 练习:
#   用户输入多个正整数,输入小于0的数时结束,
#   1)输出这些数的和
#   2)输出这些数最大和第二大的数
#   3)删除最小的一个数
#   4)按原来输入顺序打印出剩余的这些数
# s=s1=[]
# while True:
#     num=int(input('please input int:'))
#     if num<0:
#         break
#     s+=[num]
# print('输入的数总和:',sum(s))
# s1=s.copy()
# s1.sort(reverse=True)
# print('最大:',s1[0],'第二大:',s1[1])
# a=s1.pop()
# b=s.index(a)
# del s[b]
# print(s)

# 练习:
#   有字符串'hello',生成'h e l l o'和'h-e-l-l-o'
# ' '.join('hello')
# '-'.join('hello')

# 用列表推导式生成1-100内奇数的列表
# print([x for x in range(101) if x%2==1])
# print([x**2 for x in range(1,10) if x%2==1])
# begin=int(input('int1:'))
# end=int(input('int2:'))
# print([x for x in range(begin,end+1) if 
#     (x**2+1)%5==0])

# 练习:
#   1.输入一个整数n代表结束的数,求将1-n之间所有素数
#   计算出来并存入列表,打印此列表中全部的素数,打印这些
#   素数的和
# num=int(input('please input int:'))
# list=[]
# for i in range(2,num):
#     for j in range(2,i-1):
#         if i%j == 0:
#             break
#     else:
#         list.append(i)
# print(list,sum(list))

#   2.求100以内有哪些整数与自身+1的乘积再对11求余的
#   结果等于8,打印这些数存于列表中(用推导式)
# print([x for x in range(100) if 
#     x*(x+1)%11 == 8])

#   3.计算20个斐波那契数(fabonaci)存于列表并打印
#   (1,1,2,3,5,8,13....)
# list=[1,1]
# for i in range(1,19):
#     list.append(list[i-1] + list[i])
# print(list)


