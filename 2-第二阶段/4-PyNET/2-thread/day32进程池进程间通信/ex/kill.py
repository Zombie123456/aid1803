import os 
import signal 

# 向9106进程发送SIGKILL信号
os.kill(9106,signal.SIGKILL)