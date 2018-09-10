# udp_broadcast_recv.py
from socket import *
from time import sleep
host = ''
port = 9999
addr = (host, port)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(addr)

while True:
    try:
        sleep(1)
        msg, ddr = s.recvfrom(2048)
        print('getted msg: ', msg.decode())
        s.sendto(b'I am here', ddr)
    except Exception as e:
        print(e)
s.close()
