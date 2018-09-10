#!/usr/bin/env python3
#coding=utf-8
'''
name:Li Leo
data:2018-5-29
email:2938129812@qq.com
MODULES:python3.5 mysql pymysql
This is a dict project
'''
import pymysql
import re
from socketserver import *
import json
import warnings

class Server(ForkingTCPServer):
    '''
    自动生成一个多进程TCP服务器类
    '''
    pass


class Handler(StreamRequestHandler):
    '''
    用于处理客户端请求
    '''
    def handle(self):
        # print("connect from ",self.client_address)
        # self.cl ient_address == self.request.getpeername()
        self.mysql_create()
        s
        while True:
            data = self.request.recv(1024).decode()
            if data:
                l = data.split()
                if l[0] == 'L':
                    self.login(l)
                elif l[0] == 'R':
                    self.register(l)
                elif l[0] == 'Q':
                    self.query(l)
                elif l[0] == 'H':
                    self.history(l)

    def login(self,l):
        '''
        用于处理客户端的登录操作
        type:List[str]
        '''
        try:
            if len(l) != 3:
                raise
            self.cur.execute("select passwd from user \
                                     where name='%s';" % l[1] )
            data = self.cur.fetchall()
            for i in data:
                if i==(l[2],):
                    self.request.send(b'OK')
                    break
        except:
            self.request.send(b'FALL')

    def register(self,l):
        '''
        用于处理客户端的注册操作
        type l:List[str]
        '''
        try:
            self.cur.execute("insert into user values('%s','%s')" 
                              % (l[1],l[2]))
            self.db.commit()
            if len(l) != 3:
                raise
        except:
            self.db.rollback()
            self.request.send(b'FALL')
        else:
            self.request.send(b'OK')

    def query(self,l):
        try:
            self.cur.execute("select mean from words \
                                     where word='%s';" % l[1] )
            data = self.cur.fetchall()
            s = 'OK  ' + data[0][0] 
            self.request.send(s.encode())
        except:
            self.request.send(b'FALL')
        else:
            self.cur.execute("insert into hist (name,word)\
                values ('%s','%s')"% (l[2],l[1]))

    def history(self,l):
        try:
            self.cur.execute("select * from hist \
                          where name='%s';" % l[1] )
            data = self.cur.fetchall()
            print(0)
            l=[]
            s = ''
            for i in data:
                l += i
            print(1)
            j = 0
            for i in range(len(data)):
                s += l[i+j] + '  ' + l[i+1+j] + '  ' + '%s' % l[i+2+j] + '  '
                j += 2
            print(2)
            s = 'OK  ' + s
            self.request.send(s.encode())
        except:
            self.request.send(b'FALL')
 
    def mysql_create(self):
        '''
        用于创建mysql的库,表
        '''
        self.db = pymysql.connect("localhost","root","123456",
                              charset="utf8")
        self.cur = self.db.cursor()
        self.cur.execute("create database if not exists dict default charset='GBK';")
        self.cur.execute("use dict;")
        self.cur.execute("create table if not exists user (name varchar(20),\
                          passwd varchar(20),unique(name));")
        self.cur.execute("create table if not exists hist (name varchar(20),\
                          word varchar(10),\
                          time timestamp);")
        self.cur.execute("create table if not exists dict (word varchar(15),\
                          mean text);")
        self.db.commit()
        data = self.cur.execute("select * from words;")
        if not data:
            self.insert_words()

    def insert_words(self):
        '''
        用于将单词导入数据库
        '''
        self.cur.execute("use dict;")
        f = open('word.txt')
        for line in f:
            l = re.split('[ ]+', line)
            sql = "insert into words values('%s','%s')"%(l[0],' '.join(l[1:]))
            try:
                self.cur.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
        f.close()


def main():
    warnings.filterwarnings('ignore')
    # 使用创建的服务器类来生产服务器
    server = Server(('127.0.0.1', 8888), Handler)
    # 运行服务器
    server.serve_forever()


if __name__ == '__main__':
    main()
