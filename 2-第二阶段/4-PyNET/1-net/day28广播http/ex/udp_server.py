# udp_server.py
import sys
from time import ctime
from socket import *
port = int(sys.argv[2])
ip = sys.argv[1]
addr = (ip, port)
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(addr)

while True:
    print('wait for connect...')
    while True:
        data, addr = sockfd.recvfrom(1024)
        print('conect from', addr)
        if not data:
            break
        print(data.decode())
        sockfd.sendto(('%s confirm' % ctime()).encode(),
                      addr)
sockfd.close()
