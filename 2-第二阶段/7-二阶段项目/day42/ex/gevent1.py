# gevent1.py
import gevent
from gevent import monkey
from time import ctime

monkey.patch_all()
from socket import *

def server(port):
    s = socket()
    s.bind(('0.0.0.0',port))
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('connect from', addr)
        gevent.spawn(handler, c)


def handler(c):
    while True:
        data = c.recv(1024).decode()
        print('recv:',data)
        c.send(ctime().encode())
    c.close()

if __name__ == '__main__':
    server(8080)
    

