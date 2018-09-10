# exercise.py
class Mylist(list):
    def insert_head(self, element):
        self.insert(0, element)


myl = Mylist(range(3, 6))
print(myl)
myl.insert_head(2)
print(myl)
