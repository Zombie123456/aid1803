# # 最小值.py

# # 循环比较法求最小值


# def M(a):
#     m = a[0]
#     for i in range(1, len(a)):
#         if a[i] < m:
#             m = a[i]
#     return m


# a = [4, 1, 3, 5]
# print(M(a))

# # 最小值_递归


# def M(a):
#     print(a)
#     if len(a) == 1:
#         return a[0]
#     return (min(a[len(a) - 1], M(a[0:len(a) - 1])))


# l = [4, 1, 3, 5]
# print(M(l))

# # 最小值_分治


# def M(a):
#     print(a)
#     if len(a) == 1:
#         return a[0]
#     return(min(M(a[:len(a) // 2]), M(a[len(a) // 2:len(l)])))


# l = [4, 1, 3, 5]
# print(M(l))

# # 最大值和最小值_分治
# b = [3, 8, 9, 4, 10, 5, 1, 17]


# def smm(a):
#     if len(a) == 1:
#         return a[0], a[0]
#     elif len(a) == 2:
#         return min(a), max(a)
#     m = len(a) // 2
#     lmin, lmax = smm(a[:m])
#     rmin, rmax = smm(a[m:])
#     return min(lmin, rmin), max(lmax, rmax)


# print('最小和最大:%d,%d' % smm(b))
