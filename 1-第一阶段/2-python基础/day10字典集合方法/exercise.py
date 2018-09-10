# 输入一个字符串,代表星期几(0-6),'0'/'日'周日,
# '1'/'一'周一,依次类推.
# 任意输入字符串,打印这个字符串是否代表星期几.
# 如果不是以上字符打印'无相应数据'
# (以上数据存于字典中,键为字符串'0123456一二...'中的一个)
# 值为星期几或周几
# d={'0':'星期天','1':'星期一','2':'星期二',
# '3':'星期三','4':'星期四','5':'星期五',
# '6':'星期六','日':'星期天','一':'星期一',
# '二':'星期二','三':'星期三','四':'星期四',
# '五':'星期五','六':'星期六'}
# i=input('please enter:')
# print(d.get(i,'无相应数据'))

# 练习:
#   1.l=['tarena','xiaozhang','hello']
#   用字典推导式生成d={'tarena':6,
#   'xiaozhang':9,'hello':5}
# l=['tarena','xiaozhang','hello']
# d={x:len(x) for x in l}
# print(d)

#   2.no=[1001,1002,1003,1004]
#   name=['tom','jerry','spike','tyke']
#   用no作为键,name作为值生成字典
# no=[1001,1002,1003,1004]
# name=['tom','jerry','spike','tyke']
# d={no[x]:name[x] for x in range(4)}
# print(d)

# 经理有:曹操,刘备,周瑜
# 技术员有:曹操,周瑜,赵云,张飞
#   1.既是经理又是技术员
#   2.是经理不是技术员
#   3.是技术员不是经理
#   4.张飞是经理吗?
#   5.身兼一职的有谁
#   6.经理和技术员共有几人?
# s1={'曹操','刘备','周瑜'}
# s2={'曹操','周瑜','赵云','张飞'}
# print(s1&s2)
# print(s1-s2)
# print(s2-s1)
# print('张飞'in s1)
# print(s1^s2)
# print(len(s1|s2))

# 练习:
#   1.输入一段字符串,打印所有输入过的字符串,
#   不要求顺序
# s=input('please enter:')
# print(set(s))

   # 2.输入一段字符串,打印字符串出现过的字符及出现的次数
# s=input('please enter:') 
# print({x:s.count(x) for x in s })

# 练习:
#   1.猴子吃桃吃一半再吃1个,第10天剩1个,第一天有几个?
# n=1
# for i in range(9):
#     n=(n+1)*2
# print(n)

#   2.完全数1+2+3=6,1,2,3都是6的因数,
#   求4-5个完全数并打印
# for i in range(2,10000):
#     n=1
#     for j in range(2,5001):
#         if i<=j:break
#         if i%j==0:
#             n+=j
#     if n==i:
#         print(n)
            
#   3.任意输入一个数n,代表三角形高度,打印此形状的三角形
#    如:4     1
#            121
#           12321
#          1234321
#   4.将3题打印三角形变为打印菱形
#      1
#     121
#    12321
#   1234321
#    12321
#     121
#      1
# n=int(input('please enter:'))
# s1=''
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         s=str(j)
#         print(s,end='')
#         if i==1:break
#         s1+=s
#     print(s1[(j-2)::-1],end='')
#     s1=''
#     print()
# for i in range(n-1,0,-1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         s=str(j)
#         print(s,end='')
#         if i==1:break
#         s1+=s
#     print(s1[(j-2)::-1],end='')
#     s1=''
#     print()




