# 最长递增子序列

# 最长递增子序列_动态规划


# def lis(l):
#     asc = [1] * len(l)
#     tra = [-1] * len(l)
#     for i in range(1, len(l)):
#         x = []
#         for j in range(i):
#             if l[i] > l[j]:
#                 x.append(j)
#         for k in x:
#             if asc[i] < asc[k] + 1:
#                 asc[i] = asc[k] + 1
#                 tra[i] = k
#     print('asc:', asc)
#     print('tra:', tra)
#     maxx = 0
#     for i in range(1, len(asc)):
#         if asc[i] > asc[maxx]:
#             maxx = i
#     print('最长递增子序列长度是:', asc[maxx])
#     x = [l[maxx]]
#     i = maxx
#     while tra[i] >= 0:
#         x = [l[tra[i]]] + x
#         i = tra[i]
#     print('最长递增子序列=', x)


# l = [5, 2, 4, 7, 6, 3, 8, 9]
# lis(l)

# 递归函数计算


def asc(k):
    if k == 0:
        return 1
    x = []
    for i in range(k):
        if l[k] > l[i]:
            x.append(asc(i))
    if len(x) > 0:
        return max(x) + 1
    else:
        return 1


def lis_r(l):
    x = []
    for k in range(len(l)):
        x.append(asc(k))
    print(x)
    print(max(x))


l = [5, 2, 4, 7, 6, 3, 8, 9]
lis_r(l)
# l=list(range(1,31))
# lis_r(l)
