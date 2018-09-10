from socket import *
import os
import sys
import signal
import time

FILE_PATH = "/home/tarena/aid1803/project/ftp/"


class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        filelist = os.listdir(FILE_PATH)
        # 服务器确认请求是否可以执行
        if filelist == None:
            self.connfd.send(b"FALL")
        else:
            self.connfd.send(b'OK')
        time.sleep(0.1)
        files = ''
        for filename in filelist:
            if filename[0] != '.' and os.path.isfile(FILE_PATH + filename):
                files = files + filename + '#'
        self.connfd.send(files.encode())
        print('文件列表发送完毕')

    def do_get(self, filename):
        try:
            fd = open(FILE_PATH+filename, 'rb')
        except:
            self.connfd.send(b"FALL")
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.sockfd.send(data)
        fd.close()
        print("文件发送成功")

    def do_put(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'w')
        except:
            self.connfd.send(b"FALL")
            return
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024).decode()
            if data == '##':
                break
            fd.write(data)
        fd.close()
        print("接收文件完毕")


def main():
    HOST = '176.209.102.26'
    PORT = 8888
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户端登录:", addr)
        pid = os.fork()
        if pid < 0:
            print("创建子进程失败")
            connfd.close()
            continue
        elif pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            # 接收客户端请求
            while True:
                data = connfd.recv(BUFFERSIZE).decode()
                if data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == "P":
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
                elif data[0] == "Q":
                    print("客户端退出")
                    sys.exit(0)

        else:
            connfd.close()


if __name__ == "__main__":
    main()
