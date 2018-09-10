# fork.py
import os
pid = os.fork()
if pid < 0:
    print('create process false')
# 子进程
elif pid == 0:
    print('create child process')
# 父进程
else:
    print('the parent process')
# 几乎同时运行父进程和子jincheng
print('process finish')
