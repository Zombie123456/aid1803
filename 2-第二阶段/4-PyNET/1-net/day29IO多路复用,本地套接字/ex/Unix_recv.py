# Unix_recv.py
from socket import *
# 文件已被另一端创建,需要和另一端使用同一个socket文件
server_address = './test'
try:
    s = socket(AF_UNIX)
    s.connect(server_address)
except error as e:
    print(e)
    quit()
while True:
    data = input('请输入:')
    if data:
        s.sendall(data.encode())
        data = s.recv(1024)
        print('recv msg:', data.decode())
    else:
        break
s.close()


