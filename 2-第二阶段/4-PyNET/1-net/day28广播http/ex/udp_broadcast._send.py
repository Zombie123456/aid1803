# udp_broadcast_send.py
from socket import *
from time import sleep

dst = ('176.209.102.255', 9999)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    sleep(1)
    s.sendto(b'stick', dst)
    data, addr = (s.recvfrom(1024))
    print('ok')
s.close()
