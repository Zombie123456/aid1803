# tcp_server_doc.py
from socket  import *

host = '176.209.102.26'
port = 8889 
addr = (host,port)
s = socket()
s.bind(addr)
s.listen(5)
while True:
    print("wait for connect......")
    #套接字等待客户端请求
    conn,addr = s.accept()
    print("connect from ",addr)
    f = open('test1.txt', 'wb')
    while True:
        data = conn.recv(1024)
        if not data:
            f.close()
            break
        f.write(data)
        print("接受到：",data.decode())
    n = conn.send(b"Recieved your message\n")
    print("发送了　%d 字节的数据"%n)
    #关闭套接字
    conn.close()    # 表示和客户端断开连接
    
s.close() 