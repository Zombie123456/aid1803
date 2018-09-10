# process1.py
import multiprocessing as mp
import os
import time


def th1():
    print(os.getpid(),os.getppid())
    print('eat launch')
    time.sleep(6)
    print('eat ice')


def th2():
    print(os.getpid(),os.getppid())
    print('after')
    time.sleep(5)
    print('noon')


def th3():
    print(os.getpid(),os.getppid())
    print('water')
    time.sleep(4)
    print('vegetable')


p1 = mp.Process(target=th1)
p2 = mp.Process(target=th2)
p3 = mp.Process(target=th3)

p1.start()
p2.start()
p3.start()
print('asdf',os.getpid(),os.getppid())
# 阻塞等待回收进程
p1.join()
p2.join()
p3.join()

print('+++++')
th1()
th2()
th3()