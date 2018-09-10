# 二-十进制转化
# b = input('please enter a binary number:')
# d = 0
# for i in range(len(b)):
#     if b[i] == '1':
#         weight = 2 ** (len(b) - i - 1)
#         d += weight
# print(d)

# 对二-十进制转化的改进
# b = input('please enter a binary number:')
# d = 0
# weight = 2 ** (len(b) - 1)
# for i in range(len(b)):
#     if b[i] == '1':
#         d += weight
#     weight = weight // 2
# print(d)

# 整数的十-二进制转化
# x = int(input('please enter a decimal number:'))
# r = 0
# rs = []
# while(x != 0):
#     r = x % 2
#     x = x // 2
#     rs += [r]
# for i in range(len(rs)):
#     print(rs[i], end = '')
# print()

# 整数的十-二进制转化-递归
# num = int(input('please enter a decimal number:'))


# def convert(x):
#     if x < 2:
#         return([x])
#     r = x % 2
#     return(convert(x // 2) + [r])


# rs = convert(num)
# for i in range(len(rs)):
#     print(rs[i], end='')
# print()
