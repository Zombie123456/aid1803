import socket
import sys

class CallClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def main(self):
        print('----------------')
        print('1登录 2注册 3退出')
        print('----------------')
        while True:
            a = input('请选择:')
            if a == '1':
                self.login()
            elif a == '2':
                self.register()
            elif a == '3':
                sys.exit(0)

    def login(self):
        name = input('请输入账号:')
        passwd = input('请输入密码:')
        s = 'L ' + name + ' ' + passwd
        self.sockfd.send(s.encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            self.name = name
            print('登陆成功!')
            self.erji()
        elif data == 'FALL':
            print('账号或密码输入错误!')
            self.main()
        
    def register(self):
        name = input('请输入账号:')
        passwd = input('请输入密码:')
        s = 'R ' + name + ' ' + passwd
        self.sockfd.send(s.encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            print('注册成功!')
            self.main()
        elif data == 'FALL':
            print('账号已存在或不符合规范!')
            self.main()

    def erji(self):
        print('----------------------------')
        print('1查询单词 2查询历史记录 3退出')
        print('----------------------------')
        while True:
            a = input('请选择:')
            if a == '1':
                self.query()
            elif a == '2':
                self.hist()
            elif a == '3':
                self.main()

    def query(self):
        a = input('请输入要查询的单词:')
        s = 'Q ' + a + ' ' + self.name
        self.sockfd.send(s.encode())
        data = self.sockfd.recv(1024).decode()
        if data[0:4] == 'OK  ':
            print('查询成功!')
            print(data[4:])
            self.erji()
        elif data[0:4] == 'FALL':
            print('查询失败!')
            self.erji()

    def hist(self):
        s = 'H ' + self.name
        self.sockfd.send(s.encode())
        data = self.sockfd.recv(1024).decode()
        if data[0:4] == 'OK  ':
            print('查询成功!')
            l = data[4:].split('  ')
            j = 0
            for i in range((len(l)-1)//3):
                print('name:',l[i+j],'word:', l[i+1+j],'time:', l[i+2+j])
                j += 2
            self.erji()
        elif data[0:4] == 'FALL':
            print('查询失败!')
            self.erji()


def main():
    host = '127.0.0.1'
    port = 8888
    addr = (host, port)
    sockfd = socket.socket()
    sockfd.connect(addr)
    call = CallClient(sockfd)  # 生产事件对象
    call.main()


if __name__ == '__main__':
    main()

