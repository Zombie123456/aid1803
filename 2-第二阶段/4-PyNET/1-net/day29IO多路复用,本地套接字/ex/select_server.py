# select_server.py
import sys
from socket import *
from select import *
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(10)
# 将关注的IO放入rlist
rlist = [s]
wlist = []
xlist = [s]
while True:
    r, w, x = select(rlist, wlist, xlist)
    for i in r:
        if i is s:
            connfd, addr = i.accept()
            print('connect from', addr)
            # 将新的套接字加入到关注列表
            rlist.append(connfd)
        else:
            try:
                data = i.recv(1024)
                if not data:
                    rlist.remove(i)
                    i.close()
                else:
                    print('recv from', i.getpeername(),
                          ':', data.decode())
                    wlist.append(i)
            except Exception:
                pass
    for j in w:
        j.send('习大大'.encode())
        wlist.remove(j)
    for k in x:
        if k is s:
            s.close()
            sys.exit()
