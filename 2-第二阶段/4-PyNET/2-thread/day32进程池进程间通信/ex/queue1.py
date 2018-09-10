from multiprocessing import Process,Queue 
import time

q = Queue()

def fun1():
    time.sleep(1)
    q.put("我是进程1")

def fun2():
    time.sleep(2)
    print("我是进程二",q.get())

p1 = Process(target = fun1)
p2 = Process(target = fun2)
p1.start()
p2.start()

for i in (p1,p2):
    i.join()

