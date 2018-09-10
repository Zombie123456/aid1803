# tcp_client_doc.py
from socket import *

ip = '176.209.102.26'
port = 8889
addr = (ip, port)
s = socket()
s.connect(addr)
f = open('text.txt','rb')
while True:
    data = f.read(1024)
    if not data:
        f.close()
        break
    s.send(data)
data = s.recv(1024)
print("客户端收到：", data.decode())
s.close()
