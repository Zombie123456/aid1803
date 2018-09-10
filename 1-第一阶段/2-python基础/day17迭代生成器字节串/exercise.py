# exercise.py
# l = [[2],[3,4],[5],[6,7,9],10]
# def fx(l):
#     try:
#         for x in l:
#             for j in fx(x):
#                 yield j
#                 print('s')
#     except TypeError:
#         yield l
#         print('a')
# print(list(fx(l)))

# def myodd(start,stop):
#     for x in range(start,stop):
#         if x % 2 :
#             yield x
# l=[x for x in myodd(1,10)]
# print(l)

# 练习:
#   1.用生成器函数生成斐波那契数,输出前20个数,求前30个数和
# def fibonacci(n):
#     a=1
#     b=1
#     yield a
#     yield b
#     for i in range(n-2):
#         c=a+b
#         a=b
#         b=c
#         yield c
# def main():
#     l=[]
#     for i in fibonacci(20):
#         l.append(i)
#     print(l)
#     print(sum(fibonacci(30)))
# if __name__ == '__main__':
#     main()

#   2.写程序打印杨辉三角(6层)
# def yang_triangle():


# def yang_triangle():
#     l=[1]
#     while  True:
#         yield l
#         l.append(0)
#         l=[l[i-1]+l[i] for i in range(len(l))]
# def main():
#     s=int(input('请输入杨辉三角层数:'))
#     n=0
#     for t in yang_triangle():
#         print(' '*(s-len(t)),*t)
#         n+=1
#         if n==s:
#             break
# if __name__ == '__main__':
#     main()


# yang_triangle()
# def main():
#     n=int(input('请输入杨辉三角层数:'))
#     yang_triangle(n)









