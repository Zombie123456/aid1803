import os
import sys
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print('Child process...')
    sleep(2)
    sys.exit(2)  # 子进程退出
else:
    # 非阻塞状态,循环处理查看子进程状态
    while True:  
        # waitpid非阻塞等待子进程的退出
        p, status = os.waitpid(-1, os.WNOHANG)
        sleep(0.5)
        print('Parent process..')
        print(p, status)
        print(os.WEXITSTATUS(status))
    while True:
        pass
