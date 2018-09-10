# class_variable.py
class Human:
    total_count = 0

    def __init__(self, name):
        self.name = name
        self.__class__.total_count += 1

    def __del__(self):
        self.__class__.total_count -= 1


print('当前对象的个数:', Human.total_count)
h1 = Human('张飞')
h2 = Human('赵云')
print('当前对象的个数:', Human.total_count)
del h2
print('当前对象的个数:', Human.total_count)
