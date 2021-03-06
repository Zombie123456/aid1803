from socket import *
import sys
import time


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")  # 发送请求类型
        # 接收服务器确认　OK  or  FALL
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕")
        else:
            print("文件列表请求失败")

    def do_get(self, filename):
        self.sockfd.send(("G " + filename).encode())
        # 接收服务器确认　OK  or  FALL
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename, 'w')
            while True:
                data = self.sockfd.recv(1024).decode()
                if data == '##':
                    break
                fd.write(data)
            fd.close()
            print('%s 下载完成' % filename)
        else:
            print("下载文件失败")

    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except:
            print("上传的文件不存在")
            return
        self.sockfd.send(("P " + filename).encode())
        # 接收服务器确认　OK  or  FALL
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fd.close()
            print("上传文件　%s　完成" % filename)
        else:
            print("上传文件失败")

    def do_quit(self):
        self.sockfd.send(b"Q")


def main():
    HOST = '176.209.102.26'
    PORT = 8888
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024
    sockfd = socket()
    sockfd.connect(ADDR)

    ftp = FtpClient(sockfd)  # 生产事件对象

    while True:
        print("********命令选项**********")
        print("******** list************")
        print("******** get file********")
        print("******** put file********")
        print("******** quit************")
        print("********命令选项**********")
        data = input("输入命令>>")

        if data[:4] == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)
        elif data[:4] == 'quit':
            ftp.do_quit()
            sockfd.close()
            sys.exit(0)
        else:
            print("请输入正确命令！！！")


if __name__ == "__main__":
    main()
