# exercise.py
# def div_apple():
#     while  True:
#         try:
#             x=int(input('输入苹果数:'))
#             y=int(input('输入有多少人分:'))
#             result=x/y
#             print('每人能分',result,'个')
#         except (ValueError,ZeroDivisionError) as e:
#             print('发生了',e,'错误')
#             print('please again')
#         else:
#             break
# if __name__ == '__main__':
#     div_apple()

# def get_score():
#     try:
#         a=int(input('please enter:'))
#         if not 0<=a<=100:
#             raise Exception
#     except:
#         return 0
#     else:
#         return a
# print('学生的成绩:',get_score())

# 练习:
#   1.一个球从100米高度落下,每次落地后高度为原高度的一半,再落下,
#   算出第10次落地后反弹高度是?球共经过多少路径?
# def ball_down():
#     n=100
#     a=0
#     for i in range(1):
#         a+=n
#         n=n/2
#         a+=n
#     print('高度:',n,'\n路径',a)
# ball_down()

#   2.打印九九乘法表
# def multi_table():
#     for i in range(1,10):
#         print()
#         for j in range(1,i+1):
#             print('%d*%d=%d' % (i,j,i*j),end='\t')
#         print()
# multi_table()

#   3.分解质因数,输入一个正整数,分解质因数
# l1=[]
# a=0
# n=int(input('please enter integer:'))
# def prime():   
#     s=n
#     return prime_factor(s)
# def prime_factor(s):
#     global a,n
#     if a==1:
#         print(n,'=','*'.join(l1))
#         quit()
#     for i in range(2,s+1):
#         if s%i==0:
#             a=s//i
#             l1.append(str(i))
#             prime_factor(a)
# prime()








