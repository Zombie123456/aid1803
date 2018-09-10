# httpserver.py
# 静态网页处理器
# 采用循环的模式,无法满足客户端长连接
from socket import *

# 处理客户端请求
def handle_client(connfd):
    request = connfd.recv(2048)
    print(request.decode())
    # requestHeadlines = request.splitlines()
    try:
        f = open('tarena.html', 'r')
    except IOError:
        response = 'HTTP/1.1 404 notfound\r\n'
        response += '\r\n'
        response += '====sorry,fole not find'
    else:
        response = 'HTTP/1.1 200 ok\r\n'
        response += '\r\n'
        for i in f:
            response += i
    finally:
        connfd.send(response.encode())
        connfd.close()
        f.close()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8000))
    s.listen(5)
    while True:
        connfd, addr = s.accept()
        handle_client(connfd)


if __name__ == '__main__':
    main()
