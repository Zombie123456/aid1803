import time
from socket import *

while True:
    #要链接的服务器的地址信息
    HOST = '0.0.0.0'
    PORT = 8080 
    ADDR = (HOST, PORT)
    #创建客户端套接字要和访问的服务器的套接字类型相同
    connfd = socket(AF_INET, SOCK_STREAM)
    #链接服务器 
    connfd. connect (ADDR)
    while True:
        data = input("发送>>")
        if not data:
            connfd.sendall(b'client exit')
            break
        # 和服务器进行通信
        connfd.sendall(data.encode())
        data = connfd.recv(1024)
        print("客户端收到：", data.decode())
        # time.sleep(2)
    # 关闭套接字
    connfd.close() # 和服务器断开链接

