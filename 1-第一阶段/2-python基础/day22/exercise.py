# exercise.py
# 实现文件的复制(建议使用二进制方式操作)
# $ Python3 mycp.Py
#   请输入源文件: /etc/passwd
#   请输入目标文件: ./mypass.txt
#   提示'文件复制成功或失败'
#   建议使用with语句打开文件
# def mycp():
#     s1 = input('请输入源文件:')
#     s2 = input('请输入目标文件:')
#     try:
#         with open(s1, 'rb') as f, \
#                 open(s2, 'wb') as f1:
#             while True:
#                 s = f.read(4096)
#                 if not s:
#                     break
#                 f1.write(s)
#     except:
#         print("复制失败!")
#     print('复制成功')
# mycp()

# class Mylist:
#     def __init__(self, iterable):
#         self.data = [x for x in iterable]
#     def __str__(self):
#         return 'Mylist({})'.format(self.data)
#     def __add__(self, rhs):
#         return Mylist(self.data + rhs.data)
#     def __mul__(self, rhs):
#         return Mylist(self.data * rhs)
#     def __rmul__(self, lhs):
#         return Mylist(lhs * self.data)
#     def __iadd__(self, lhs):
#         self.data.extend(lhs.data)
#         return self # 已改变self
# L1 = Mylist([1, 2, 3])
# L2 = Mylist(range(4, 7))
# L3 = L1 + L2
# print('L3 =', L3)
# L4 = L1 * 2
# print('L4 =', L4)
# L5 = 2 * L1
# print('L5 =', L5)
# L1 += L2
# print('L1 =', L1)

# 练习:
#   实现有序集合类OrderSet(),能实现两个集合的交集&,并集|,补集-,
#   对称补集^,==,!=操作
#   集合内部用list存储


class OrderSet:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'OrderSet({})'.format(self.data)

    def __and__(self, value):
        return self & value

    # def __contains__(self, s):
    #     s in self.data

    # def __sub__(self, value):
    #     return self - value

    # def __xor__(self, value):
    #     Return self^value.


s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)
