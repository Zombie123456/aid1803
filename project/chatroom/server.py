# server.py
'''
name:levi
chatroom server
'''
import os
from socket import *
from time import ctime


def do_login(s, user, name, addr):
    if (name in user) or name == 'administrator':
        s.sendto(b'OK', addr)
        msg = '\n欢迎%s进入聊天室' % name
        # 通知所有人
        for i in user:
            if i != name:
                s.sendto(msg.encode(), user[i])
    else:
        s.sendto('用户名不存在,请注册'.encode(), addr)


def do_register(s, user, name, addr):
    if (name in user) or name == 'administrator':
        s.sendto('该用户已存在请重输'.encode(), addr)
        return
    # 将用户插入字典
    user[name] = addr
    s.sendto(b'OK', addr)


def do_chat(s, user, cmd):
    msg = '\n%s' % cmd[1]
    msg += '(%s)' % ctime() 
    msg += '\n' + ' '*2 + ' '.join(cmd[2:])
    for i in user:
        if i != cmd[1]:
            s.sendto(msg.encode(), user[i])
        else:
            data = '%+s' % msg
            s.sendto(data.encode(), user[i])


def do_quit(s, user, name):
    del user[name]
    msg = '\n' + name + '离开了聊天室'
    for i in user:
        s.sendto(msg.encode(), user[i])


def do_administrator(s, addr):
    while True:
        msg = input('管理员消息:')
        msg = 'C adiministrator' + msg
        s.sendto(msg.encode(), addr)


def handle_request(s):
    # 用字典来存储用户信息
    user = {}
    # 循环接收请求
    while True:
        data, addr = s.recvfrom(2048)
        data = data.decode()
        cmd = data.split(' ')
        if cmd[0] == 'L':
            do_login(s, user, cmd[1], addr)
        elif cmd[0] == 'R':
            do_register(s, user, cmd[1], addr)
        elif cmd[0] == 'C':
            do_chat(s, user, cmd)
        elif cmd[0] == 'Q':
            do_quit(s, user, cmd[1])
        else:
            s.sendto(b'request failed', addr)


def main():
    ip = '176.209.102.26'
    port = 8889
    addr = (ip, port)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(addr)
    # 创建一级子进程
    pid = os.fork()
    if pid < 0:
        print('create process failed')
    elif pid == 0:
        # 创建二级子进程
        p = os.fork()
        if p < 0:
            print('process failed')
        elif p == 0:
            handle_request(s)
        else:
            os._exit(0)
    else:
        os.wait()
        do_administrator(s, addr)


if __name__ == '__main__':
    main()
