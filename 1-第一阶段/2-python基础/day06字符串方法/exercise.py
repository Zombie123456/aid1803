# 练习:
#   输入一个字符串:
#   1.判断输入的字符串有几个字符'e'
#   2.判断输入的有几个空格
#   3.判断输入的字符串是否以'?'结尾
# s=input('please input str:')
# print('字符e的个数:',s.count('e'))
# print('space的个数:',s.count(' '))
# print('以问号结尾?(True/False):',s.endswith('?'))

# 练习:
#   输入三行文字,让这三行文字依次以20个字符的宽度
#   右对齐输出
#   思考:能否以最20字符串的长度进行右对齐显示,左侧填充空格
# s1=input('please input str1:')
# s2=input('please input str2:')
# s3=input('please input str3:')
# i=int(max(len(s1),len(s2),len(s3)))
# c=str(i)
# #法一
# fmt='%' + str(c) + 's'
# #法二
# fmt='%%%ds' % c
# print(fmt % s1 )
# print(fmt % s2 )
# print(fmt % s3 )

# 练习:
#   1.输入一个整数n,打印n以内全部大于0的偶数,不包括n
# n=int(input('please input integer:'))
# i=1
# while i < n:
#     if i%2 == 0:
#         print(i)
#     i += 1

#   2.打印从0开始浮点数,每个数增加0.5,10以内
# i=0
# a=float(i)
# while a < 10:
#     print(a)
#     a += 0.5

#   3.打印1-20的整数,打印在一行显示.每个数字间用空格
#   分隔
# i=1
# while i <= 20 :
#     if i <= 19:
#         print(i,end=' ')
#     else:dayi
#         print(i)
#     i += 1

#   4.打印1-20的整数,每行5个,打印4行
# i=1
# while i <= 20:
#     print(i,end=' ')
#     if i%5 == 0:
#         print()
#     i += 1

#   5.用while语句打印10-1之间的整数
# i=10
# while i >= 1:
#     print(i)
#     i -= 1

#   6.用while语句打印三角形,输入一个整数,表示三角形的
#   宽度和高度
# num=int(input('please input integer:'))
# i=1
# while i <= num:
#     print('*'*i)
#     i += 1

# 练习:
#   输入一个数,打印指定宽度的正方形
# a=int(input('please input integer:'))
# for i in range(1,a + 1):
#     for i in range(1,a + 1):
#         print(i,end=' ')
#     print()

# 练习:
#   1.打印三角形,输入一个整数,表示三角形的宽度和高度
#   a.左对齐b.右对齐c.倒右对齐d.倒左对齐
# a=int(input('please input integer:'))
# i=j=k=m=1
# while i <= a:
#     print('*'*i)
#     i += 1
# while k <= a:
#     print(' '*(a - k)+'*'*(k))
#     k += 1
# while j <= a:
#     print(' '*(j - 1)+'*'*(a + 1 - j))
#     j += 1
# while m <= a:
#     print('*'*(a + 1 - m)+' '*(m - 1))
#     m += 1

#   2.输入一个开始的整数值用变量begin绑定,
#   输入一个开始的整数值用变量end绑定,
#   打印从begin到end(不包含)的每个整数(一行内)
#   思考:每5个数字打印在一行内
# begin=int(input('please input first integer:'))
# end=int(input('please input last integer:'))
# if begin >= end:
#     print('开始值大于或等于结束值')
# i=0
# while begin+i < end:
#     print(begin+i,end=' ')
#     i += 1
#     if i%5 == 0:
#         print()
#     if begin + i == end:
#         print
# a=0
# for i in range(begin,end):
#     print(i,end='\t')
#     a += 1
#     if a%5 == 0 or i == end-1:
#         print()

#   3.用while循环生成如下字符串:
#   a.'ABCDEFG...XYZ'并打印
#   b.生成'AaBb.....YyZz'并打印
#   提示:
#     用chr和ord()
# i=j=1
# while i <= 26 :
#     print(chr(i + 64),end='')
#     i += 1
#     if i == 27:
#         print()
# while j <= 26:
#     print('{}{}'.format(chr(j + 64),
#         chr(96 + j)),end='')
#     j += 1
#     if j == 27:
#         print()




