# condition.py
import threading
import time
import datetime

num = 0

con = threading.Condition()


class Gov(threading.Thread):
    def run(self):
        global num
        con.acquire()
        while True:
            print('牛市')
            num += 1
            print('上涨到%s点' % num)
            time.sleep(2)
            if num >= 5:
                print('暂时安全')
                con.notify()
                print('不操作')
                con.wait()
        con.release()


class Consumers(threading.Thread):
    def run(self):
        global num
        con.acquire()
        while True:
            if num > 0:
                print('熊市')
                num -= 1
                print('下调到%s个点' % num)
                time.sleep(2)
                if num == 0:
                    print('去天台')
                    con.notify()
                    print('没有下降空间了')
                    con.wait()
        con.release()


t1 = Gov()
t2 = Consumers()
t1.start()
t2.start()
