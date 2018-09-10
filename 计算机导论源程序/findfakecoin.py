# # 找假币的第一种方法
# def findcoin_1(l):
#     if len(l) <= 1:
#         print('error:coin are too few')
#         quit()
#     i = 0
#     while i < len(l):
#         if l[i] < l[i + 1]:
#             return (i)
#         elif l[i] > l[i + 1]:
#             return (i + 1)
#         i += 1
#     print('all coins are too same')
#     return len(l)


# import random
# n = int(input('enter the number of coin >= 2:'))
# w_normal = random.randint(2, 5)
# index_faked = random.randint(0, n - 1)
# l = []
# for i in range(n):
#     l.append(w_normal)
# l[index_faked] = w_normal - 1
# print(l)
# print('the index of faked coin:', findcoin_1(l))

# # 二分法找假币


# def findcoin(a, l):
#     x = len(l)
#     print(a, l)
#     if x == 1:
#         return a
#     if x % 2 == 1:
#         x = x - 1
#         y = 1
#     else:
#         y = 0
#     if sum(l[:x // 2]) < sum(l[x // 2:x]):
#         return findcoin(a, l[:x // 2])
#     elif sum(l[:x // 2]) > sum(l[x // 2:x]):
#         return findcoin(a + x // 2, l[x // 2:x])
#     else:
#         if y == 0:
#             return -1
#         else:
#             if l[x] < l[0]:
#                 return a + x
#             else:
#                 return -1


# import random
# n = int(input('enter the number of coin >= 2:'))
# w_normal = random.randint(2, 5)
# index_faked = random.randint(0, n - 1)
# l = []
# for i in range(n):
#     l.append(w_normal)
# l[index_faked] = w_normal - 1
# print('the index of faked coin:', findcoin(n, l))
