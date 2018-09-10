# 练习:
#   任意输入一个字符串,将此字符串中的空格全部去掉,生成
#   反转后的字符串
# s=input('please input:')
# #法一 空格拆分法
# l=s.split(' ')
# #s1=''.join(l)
# for i in range(len(l)):
#     s1=l[i-1]+l[i]
# print(s1[::-1])
# #法二替换法
# s1=s.replace(' ','')
# print(s1[::-1])
# #法三
# l=[]
# for x in reversed(s):
#     if x!=' ':
#         l.append(x)
# s1=''.join(l)
# print(s1)

# 练习:
#   1.算出100-999内的水仙花数(narcissistic number)
#   百位的立方+十位的立方+个位的立方等于原数
# l1=[]
# for i in range(100,1000):
#     b=str(i)
#     if int(b[0])**3+int(b[1])**3+int(b[2])**3==i:
#         l1.append(i)
# print(l1)

#   2.任意输入一些大于0的数存于列表,输入-1的结束
#   打印出这些数;打印出这些数的和;去掉列表l1中重复输入的数
#   (只留一个),再次存到另一个列表中;打印l2列表中的数据和;
#   将l1中出现2次的数寸照另一个列表l3中
l1=[]
l2=[]
l3=[]
while True:
    num=int(input('please enter int:'))
    if num == -1:
        break
    l1.append(num)
for i in l1:
    if not i in l2:
        l2.append(i)
for j in range(len(l1)):
    if l1.count(l1[j])==2 and (not l1[j] in l3):
        l3.append(l1[j])
print(l1,sum(l1))
print('l2:',l2)
print('l3',l3)






