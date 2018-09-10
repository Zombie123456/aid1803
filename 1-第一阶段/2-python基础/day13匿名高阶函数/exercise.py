# 写一个lambda表达式,判断这个数的2次方再加一能否被5整除,
# 能整除返回True,否则返回False
# fx=lambda n:(n**2+1)%5==0
# print(fx(4))

# 写一个lambda表达式,求两个变量的最大值:
# mymax=lambda x,y:x if x>y else y
# print(mymax(55,63))

# 写一个程序,解释执行用户输入的任何语句
# while 1:
#     s=input('输入程序:')
#     if s=='bye':break
#     exec(s)

# 求1+1/2+1/4+1/8+....+1/2**n
# n=100
# a=sum([1/2**x for x in range(n+1)])
# print(a)

# x=3
# print(sum(map(pow,range(1,10),
#     [x for i in range(9)])))

# 用filter打印10以内偶数的列表
# print([x for x in filter(lambda x:x%2==0,
#     range(10))])]

# 将列表中元素按各元素的最后一个至第一个顺序排序
# l=['tom','jerry','spike','tyke']
# print(sorted(l,key=(lambda x:x[::-1])))

# 递归
# def fx(n):
#     print('现在是',n,'层')
#     if n>=3:
#         return
#     fx(n+1)
#     print('递归的第',n,'层结束')
# fx(1)
# print('主程序结束')


# def mysum(x):
#     if x==1:return 1
#     return mysum(x-1)+x
# print(mysum(100))

# a=100
# def mysum(x):
#     global a
#     a+=x
#     if x==1:
#         print(a)
#         quit()
#     mysum(x-1)
# mysum(99)

# 练习:
#   1.myfax计算x的阶乘x!,5!=5*4*3*2*1
# def myfax(n):
#     for i in range(1,n):
#         n*=i
#     return n
# print(myfax(20))

#   2.算出1-20阶乘的和
#   思考:用高阶函数编写

# print(sum([x for x in map(myfax,range(1,21))])

#   3.已知有列表l=[[3,5,8],10,[[13,14],15],18]
#   a.print_list(lst)打印出列表中所有数字
#   b.sum_list(lst)返回列表中所有数字的和
#   注:type(x)可以返回一个变量的类型
l=[[3,5,8],10,[[13,14],15],18]
# def print_list(lst):
#     for i in range(len(lst)):
#         if type(lst[i]) is int:
#             print(lst[i])
#         else:
#             for j in range(len(lst[i])):
#                 if type(lst[i][j]) is int:
#                     print(lst[i][j])
#                 else:
#                     for k in range(len(lst[i][j])): 
#                         if type(lst[i][j][k]) is int:
#                             print(lst[i][j][k])
# l1=[]
# def print_list(lst):
#     global l1
#     for i in range(len(lst)):
#         if type(lst[i]) is int:
#             l1.append(lst[i])
#         else:
#             print_list(lst[i])

# print_list(l)
# print(l1)
# def sum_list(lst):
#     return sum(lst)
# print(sum_list(l1))

