# client.py
from socket import *
import sys
import os
import signal


def register(s, addr):
    while True:
        name = input('请输入要注册的用户名:')
        msg = 'R ' + name
        s.sendto(msg.encode(), addr)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('注册成功')
            break
        else:
            print(data.decode())
            a = input('请1(登录)其他(重新注册)')
            if a == '1':
                login(s, addr)


def login(s, addr):
    while True:
        name = input('请输入登录用户名')
        msg = 'L ' + name
        s.sendto(msg.encode(), addr)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('进入聊天室')
            return [1, name]
        else:
            print(data.decode())
            a = input('请1(注册)其他(重新登录)')
            if a == '1':
                register(s, addr)


def do_sendto(s, name, addr):
    while True:
        text = input('发言(输入quit退出):')
        if text == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit('退出聊天室')
        else:
            msg = 'C %s %s' % (name, text)
            s.sendto(msg.encode(), addr)


def do_recvfrom(s):
    while True:
        msg, addr = s.recvfrom(1024)
        print(msg.decode() + '\n发言(输入quit退出):', end='')


def main():
    ip = '176.209.102.26'
    port = 8889
    addr = (ip, port)
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        op = input('请选择1(登录)或2(注册)')
        if op == '1':
            L = login(s, addr)
            if L[0] == 1:
                break
        elif op == '2':
            register(s, addr)
    pid = os.fork()
    if pid < 0:
        print('create process failed')
    elif pid == 0:
        do_sendto(s, L[1], addr)
    else:
        do_recvfrom(s)


if __name__ == '__main__':
    main()
