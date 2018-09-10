# fork.py
import os, sys
from time import sleep
pid = os.fork()
if pid < 0:
    print('create process failed')
# 子进程
elif pid == 0:
    print('create child process',os.getpid())
    sleep(2)
    sys.exit(3)
# 父进程
else:
    p, status = os.wait()
    print(p, status)
    while True:
        pass
# 几乎同时运行父进程和子jincheng
print('process finish')
