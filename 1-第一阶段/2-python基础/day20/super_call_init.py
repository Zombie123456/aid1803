# super_call_init.py


# 此示例用于示意如何显示调用父类的初始化方法(也叫构造方法)
class Human:
    def __init__(self, n, a):
        self.name2 = n
        self.age = a

    def infos(self):
        print("姓名:", self.name2, "年龄:", self.age)


class Student(Human):
    def __init__(self, n, a, s=0):
        super().__init__(n, a)
        self.score = s

    def infos(self):
        super().infos()
        print("成绩:", self.score)
        # print("姓名:", self.name,
        #       "年龄:", self.age,
        #       "成绩:", self.score)


h1 = Human("老魏", 35)
h1.infos()

s1 = Student("小赵", 20, 100)
s1.infos()
