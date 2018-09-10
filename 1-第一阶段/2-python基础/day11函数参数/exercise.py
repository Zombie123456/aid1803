
#   1.函数mysum(),有两个参数x,y,功能是打印两个参数的和
# def mysum(x,y):
#     return x+y
# x=int(input('please enter x:'))
# y=int(input('please enter y:'))
# z=mysum(x,y)
# print(z)

#   2.print_even,传入一个数n代表终止数(不包含),
#   打印到n之间所有偶数
# n=int(input('please enter integer:'))
# def print_even(self):
#     for i in range(1,self):
#         if i%2==0:
#             print(i)
# print_even(n)

# #返回两个的最大值
# def mymax(a,b):
#     if a>b:
#         return(a)
#     else:
#         return(b)
# print(mymax('abc','acd'))

# input_number()读取多个整数,为负数时结束,输入的数
# 为列表返回
# def input_number():
#     m=[]
#     while 1:
#         n=int(input('please enter integer:'))
#         if n<0:return m
#         m+=[n]
# l=input_number()
# print('max:',max(l))
# print('sum:',sum(l))

# 练习:
#   1.mysum,可以传入任意个实参的数字,返回,所有实参的和
# def mysum(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# num=mysum(6565,44,464,45454,45454,54)
# print(num)

#   2.mymax函数,功能与max函数完全相同
# 方法一
# def mymax(*args):
#     if len(args)==1:
#         l=list(*args)
#     elif len(args)>1:
#         l=list(args)
#     l.sort()
#     return l[-1]
# 方法二
# def mymax(a,*args):
#     if len(args)==0:
#         m=a[0]
#         i=1
#         while i<len(a):
#             if a[i]>m:
#                 m=a[i]
#             i+=1
#         return m
#     else:
#         m=a
#         for x in args:
#             if x>m:
#                 m=x
#         return m
# 方法三
# def mymax(a,*args):
#     def mmax(*args):
#         m=args[0]
#         i=1
#         while i<len(args):
#             if args[i]>m:
#                 m=args[i]
#             i+=1
#         return m
#     if len(args)==0:
#         return mmax(*a)
#     return mmax(a,*args)
# print(mymax([12,25,35,15,12,1,158]))
# print(mymax(100,200))
# print(mymax(range(10)))


#   3.minmax()函数,给出任意个数字实参,返回最小和最大数
#   要求2个数字形成元组后返回(小,大)
#   xiao,da=minmax()
#   print('min:',xi4ao)
#   print('max:',da)
