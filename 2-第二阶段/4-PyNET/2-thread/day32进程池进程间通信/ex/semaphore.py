# semaphore.py
from multiprocessing import *
from time import sleep

sem = Semaphore(3)

def fun():
    print('进程%s等待信号量' % current_process())
    sem.acquire()
    print('进程%s消耗信号量' % current_process())
    sleep(3)
    print('进程%s添加信号量' % current_process())
    sem.release()

jobs = []
for i in range(4):
    p = Process(target = fun)
    p.start()
    jobs.append(p)

for i in jobs:
    i.join()
