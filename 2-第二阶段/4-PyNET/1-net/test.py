# test.py
from socket import socket
from time import ctime, sleep
# tcp_server
# ip = '176.209.102.26'
# port = 8889
# addr = (ip,port)
# s = socket(AF_INET, SOCK_STREAM, 0)
# s.setsockopt(SOL_SOCKET, SO_REUSERADDR, 1)
# s.bind(addr)
# s.listen(5)
# while True:
#     print('wait for connect...')
#     connfd, addr = s.accept()
#     print('connect for', addr)
#     while True:
#         data = connfd.recv(1024)
#         if not data:
#             break
#         print('recv msg:', data.decode())
#         connfd.send(b'xidada')
#     connfd.close()

# tcp_client
# ip = '176.209.102.26'
# port = 8889
# addr = (ip,port)
# s = socket(AF_INET, SOCK_STREAM, 0)
# s.connect(addr)
# while True:
#     data = input('发送:')
#     if not data:
#         s.send(b'client exit')
#         break
#     s.send(data.encode())
#     data = s.recv(1024)
#     print('recv msg:', data.decode())
# s.close()

# udp_server
# ip = '176.209.102.26'
# port = 8889
# addr = (ip, port)
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_REUSERADDR, 1)
# s.bind(addr)
# while True:
#     print('wait for connect...')
#     while True:
#         data, addr = s.recvfrom(1024)
#         if not data:
#             break
#         print('recv msg:', data.decode(), 'from', addr)
#         s.sendto(b'confirm', addr)
# s.close()

# udp_client
# ip = '176.209.102.26'
# port = 8889
# addr = (ip, port)
# s = socket(AF_INET, SOCK_DGRAM)
# while True:
#     data = input('发送:')
#     if not data:
#         s.sendto('client exit', addr)
#         break
#     s.sendto(data.encode(), addr)
#     data, addr = s.recvfrom(1024)
#     print('recv msg:', data.decode(), 'from', addr)
# s.close()

# udp_broadcast_send
# ip = '176.209.102.255'
# port = 8889
# addr = (ip, port)
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# while True:
#     sleep(1)
#     s.send(b'xidada', addr)
#     data, addr = s.recvfrom(1024)
#     print('recv msg:', data.decode(),
#           'from', addr)
# s.close()

# udp_broadcast_recv
# ip = ''
# port = 8889
# addr = (ip, port)
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_REUSERADDR, 1)
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# s.bind(addr)
# while True:
#     try:
#         sleep(1)
#         data, addr = s.recvfrom(1024)
#         print('recv msg:', data.decode())
#         s.sendto(b'I am here', addr)
#     except:
#         pass
# s.close()
