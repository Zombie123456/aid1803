# tcp_server.py
import socket

sockfd = socket.socket(AF_INET, SOCK_STREAM, 0)
sockfd.bind(("127.0.0.1", 8888))
sockfd.listen(5)
connfd, addr = sockfd.accept()
data = connfd.recv(1024)
connfd.send(b'hello,world!')
connfd.close()
sockfd.close()
