# mysum函数作用是返回1至n的和
# def mysum(n):
#     s=0
#     for i in range(n+1):
#         s+=i
#     return s
# print(mysum(100))

# mysum2函数,可以传入一个参数,2个参数,和三个参数:
# 传入一个参数时代表终止数,传入2个参数时,第一个参数代表起始值,
# 第二个参数代表终止值;传入3个参数时,第三个参数代表步长
# 功能是返回从开始到终止的和
# 法一
# def mysum2(a,b=0,c=1):
#     if a>b:a,b=b,a
#     return sum(range(a,b,c))
# 法二
# def mysum2(*args):
#     return sum(range(*args))
# print(mysum2(5))
# print(mysum2(4,6))
# print(mysum2(5,10,2))

# 练习:
#   1.创建一个列表l=[],写函数input_number
#   读取数据放入列表l中
# l=[]
# def input_number():
#     global l
#     while True: 
#         i=int(input('please enter number:'))
#         if i == -1:break
#         l+=[i]
#     return l
# input_number()
# print('刚输入的整数值是:',l)

# 2.函数isprime(x)判断x是否是素数,为素数返回True,
# 否则False
# def isprime(x):
#     if x < 2:return False
#     for i in range(2,int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     else:
#         return True
# if isprime(5):
#     print('5 is prime')

# 3.prime_m2n(m,n)返回从m开始,n结束范围内的素数列表,
# 并打印
# def prime_m2n(m,n):
#     l1=[]
#     if m<2:m=2
#     for i in range(m,n):
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:break
#         else:
#             l1.append(i)
#     return l1
# l=prime_m2n(10,20)
# print(l)#[11,13,17,19]

# 4.primes(n),返回小于n的所有素数列表
# def primes(n):
#     l1=[]
#     for i in range(2,n):
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:break
#         else:
#             l1.append(i)
#     return l1
# l=primes(10)
# print(l)#[2,3,5,7]


