# exercise.py
# class Student:
#     def __init__(self, n, a, s):
#         self.name, self.age, self.score = n, a, s

#     def set(self):
#         l = [self.name] + [self.age] + [self.score]
#         return l


# def input_student():
#     l = []
#     while True:
#         n = input('请输入学生姓名:')
#         if not n:
#             break
#         a = int(input('请输入学生年龄:'))
#         s = int(input('请输入学生成绩:'))
#         d = Student(n, a, s)
#         l.append(d)
#     return l


# def output_student(l):
#     for i in l:
#         print('姓名:%s 年龄:%d 成绩:%d' % (i.name, i.age, i.score))


# def main():
#     l = input_student()
#     output_student(l)


# if __name__ == '__main__':
#     main()

class Human:
    count = 0

    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad
        self.__class__.count += 1

    def __del__(self):
        self.__class__.count -= 1

    def show_info(self):
        print('姓名:', self.name,
              '年龄:', self.age,
              '地址:', self.address)

    def update_age(self):
        self.age += 1

    @classmethod
    def get_human_count(cls):
        return cls.count


def input_human():
    L = []
    while True:
        n = input('请输您的姓名(或输入回车结束):')
        if not n:
            break
        a = int(input('请输入您的年龄:'))
        ad = input('请输入您住址:')
        info = Human(n, a, ad)
        L.append(info)
    return L


def main():
    docs = input_human()
    print('总人数:', Human.get_human_count())
    docs += input_human()
    print('总人数:', Human.get_human_count())
    # for h in docs:
    #     h.show_info()
    # for h in docs:
    #     h.update_age()
    # for h in docs:
    #     h.show_info()


if __name__ == '__main__':
    main()
