# Unix_send.py
from socket import *
import os

# 确定用哪个文件通信
server_address = './test'
# 判断文件存在性,若已存在需处理
if os.path.exists(server_address):
    os.unlink(server_address)
# 创建本地套接字
s = socket(AF_UNIX)
# 绑定本地套接字文件
s.bind(server_address)
# 监听
s.listen(5)
# 收发消息
while True:
    c, addr = s.accept()
    while True:
        data = c.recv(1024)
        if data:
            print('recv msg:', data.decode())
            c.sendall('recv msg'.encode())
        else:
            break
    c.close()
s.close()


