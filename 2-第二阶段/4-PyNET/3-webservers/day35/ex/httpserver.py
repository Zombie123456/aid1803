# httpserver.py
'''
完成httpserver的并发
并发使用多线程完成
用不同的后端程序处理不同的请求
可以简单的显示静态页面
'''
from socket import *
from threading import Thread
import sys

ADDR = ('0.0.0.0', 8000)
STATIC_HANDLE = './html'
HANDLE_PYTHON = './handle'

class HttpServer:
    def __init__(self,addr):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        self.serve_name = '127.0.0.1'
        self.serve_port = 8000

    # 服务器启动函数:接收客户端请求,创建新的线程
    def server_forever(self):
        while True:
            self.connfd, self.client_addr = self.sockfd.accept()
            client_thread = Thread(target=self.handle_request)
            client_thread.start()

    def handle_request(self):
        self.recvdata = self.connfd.recv(2048)
        request_head = self.recvdata.splitlines()
        for line in request_head:
            print(line)
        # 获取从浏览器输入的具体请求
        getrequest = str(request_head[0]).split(' ')[1]
        if getrequest[-3:] != '.py':
            if getrequest == '/':
                getfilename = STATIC_HANDLE + '/index.html'
            else:
                getfilename = STATIC_HANDLE + getrequest
            try:
                f = open(getfilename)
            except:
                response_heads = 'HTTP/1.1 404\r\n'
                response_heads += '\r\n'
                response_body = '=====sorry,file not find====='
            else:
                response_heads = 'HTTP/1.1 200 OK\r\n'
                response_heads += '\r\n'
                response_body = f.read()
                f.close()
            finally:
                response = response_heads + response_body
                self.connfd.send(response.encode())
        else:
            # 需要的环境变量
            env = {}
            body_content = self.application(env, self.start_response)
            response = 'Http/1.1 {}\r\n'.format(self.header_set[0])
            for header in self.header_set[1:]:
                response += '{}:{}\r\n'.format(*header)
            response += '\r\n'
            response += body_content
            self.connfd.send(response.encode())
        self.connfd.close()

    def start_response(self, status, response_heads):
        server_headers = [('Date', '2018-5-21'),
                          ('Server', 'HttpServer 1.0')]
        self.header_set = [status, response_heads + server_headers]

    def setapp(self, application):
        self.application = application


def main():
    # 启动时,直接告诉使用哪个模块,函数处理请求
    # python3 httpserver.py module app
    if len(sys.argv) < 3:
        sys.exit('请选择一个模块和应用')
    # 将handle加入搜索路径
    sys.path.insert(0, HANDLE_PYTHON)
    # 导入module模块
    m = __import__(sys.argv[1])
    # 获取模块下要使用的app,赋值给一个变量
    application = getattr(m, sys.argv[2])

    httpd = HttpServer(ADDR)
    httpd.setapp(application)
    print('Servering HTTP on port 8000')
    httpd.server_forever()


if __name__ == '__main__':
    main()
