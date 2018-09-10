# 练习:
#   用for语句求出一段字符中空格个数
#   用while实现
# s=input('please input str:')
# count=0
# for i in s:
#     if i == ' ':
#         count += 1
# print('space number:',count)
# i=0
# while i < len(s):
#     if ' ' == s[i]:
#         count += 1
#     i += 1
# print(count)

# 练习:
# 1.用for循环生成如下字符串:
#   a.'ABCDEFG...XYZ'并打印
#   b.生成'AaBb.....YyZz'并打印
#   提示:
#     用chr和ord()
# for i in range(65,91):
#     print(chr(i),end='')
# print()
# for j in range(1,27):
#     print(chr(j+64)+chr(j+96),end='')
# print()

# 2.用for循环嵌套打印矩形,输入数n,代表宽度及高度
#  1 2 3 4 5
#  2 3 4 5 6
#  3 4 5 6 7 
#  4 5 6 7 8
#  5 6 7 8 9
# num=int(input('please input integer:'))
# for i in range(1,num + 1):
#     for j in range(i,num + i):
#         print(j,end=' ')
#     else:
#         print()
# print()

# 输入若干行,以直接回车结束 并打印
# L=[]
# while 1:
#     s=input('input:')
#     if len(s)==0:
#         break
#     L+=[s]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# print(L)

# 练习:
#  1.输入一个unicode的开始值用begin绑定,结束值用stop
#  绑定,打印开始到结束的所有对应的文字
# begin=int(input('please input first int:'))
# stop=int(input('please input stop int:'))
# if begin>=stop:
#     print(error)
# for i in range(begin,stop+1):
#     print(chr(i),end='')
# print()

#  2.输入一个整数(代表树干及树冠的高度),打印一棵树
# num=int(input('please input int:'))
# for i in range(1,num+1):
#     print(' '*(num-i)+'*'*(2*i-1))
# for j in range(1,num+1):
#     print(' '*(num-1)+'*')

#  3.打印树,*号用数字代替,树干用*,数字最高9
# num=int(input('please input int:'))
# for i in range(1,num+1):
#     print(' '*(num-i)+str(i)*(2*i-1))
# for j in range(1,num+1):
#     print(' '*(num-1)+'*')

#  4.输入一个正整数,打印这个数是否是素数(prime)
# num=int(input('please input int:'))
# if num==1:
#     print('不是素数')
# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print('不是素数')
#             break
#     else:
#         print('是素数')




