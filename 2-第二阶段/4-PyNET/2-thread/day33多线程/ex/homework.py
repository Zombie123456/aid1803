# homework.py
from multiprocessing import Process
from signal import *
import os
from time import sleep


def seller_handler(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print('到站了,下车吧')
        print('售票员下车')
        os._exit(0)


def driver_handler(sig, frame):
    if sig == SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('系好安全带,小心甩出去')
    elif sig == SIGTSTP:
        os.kill(seller.pid, SIGUSR1)
        sleep(0.1)
        print('司机下车')


def ticket_seller():
    signal(SIGQUIT, seller_handler)
    signal(SIGINT, seller_handler)
    signal(SIGUSR1, seller_handler)
    signal(SIGTSTP, SIG_IGN)
    while True:
        sleep(1)


seller = Process(target=ticket_seller)
seller.start()
signal(SIGQUIT, SIG_IGN)
signal(SIGINT, SIG_IGN)
signal(SIGTSTP, driver_handler)
signal(SIGUSR1, driver_handler)
signal(SIGUSR2, driver_handler)
seller.join()
