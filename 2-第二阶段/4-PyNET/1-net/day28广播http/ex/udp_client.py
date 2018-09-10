# udp_client.py
import sys
from socket import *
ip = sys.argv[1]
port = int(sys.argv[2])
addr = (ip,port)
sockfd = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('please enter:')
    if not data:break
    sockfd.sendto(data.encode(), addr)
    data, addr = sockfd.recvfrom(1024)
    print('recv msg:',data.decode())
sockfd.close()

