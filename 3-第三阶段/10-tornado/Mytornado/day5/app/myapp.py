import time
import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule
from util.myutil import mymd5
from util.dbutil import DBUtil

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        msg = self.get_query_argument('msg', None)
        self.render('login.html',msg=msg)

    def post(self, *args, **kwargs):
        pass


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username',None)
        password = self.get_body_argument('password',None)
        password = mymd5(password)
        dbutil = DBUtil()
        # result = cursor.fetchone()
        if dbutil.is_login(username,password):
            #跳转到blog页面
            self.redirect('/blog?username='+username)
        else:
            #跳转回登录界面
            self.redirect('/?msg=用户名或密码错误')


class registerHandler(RequestHandler):
    def get(self):
        msg = self.get_query_argument('msg', None)
        self.render('register.html',msg=msg)

    def post(self):
        uname = self.get_body_argument('uname',None)
        upwd = self.get_body_argument('upwd',None)
        ucity = self.get_body_argument('ucity',None)
        if uname and upwd and ucity:                   
            if self.request.files:
                avatar = None
                f = self.request.files['avatar'][0]
                body = f['body']
                fname = str(time.time()) + f['filename']
                writer = open('mystatics/images/%s' % fname,'wb')
                writer.write(body)
                writer.close()
                avatar = fname
            upwd = mymd5(upwd)
            dbutil = DBUtil()
            try:
                dbutil.save_user(uname,upwd,avatar,ucity)
                self.redirect('/')
            except Exception as e:
                if avatar:
                    os.remove('mystatics/images/%s' % avatar)
                err =str(e)             
                self.redirect('/register?msg='+err)
        else:
            self.redirect('/register?msg=有未输入的项')
        

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('blog.html')

    def post(self, *args, **kwargs):
        pass

    def initialize(self):
        '''让继承者在执行get/post方法之前传入参数
        或者执行一些初始化操作'''
        pass

    def set_default_headers(self):
        '''用来设置自定义响应头'''
        pass

    def on_finish(self):
        '''执行get/post方法后,释放资源'''
        pass


class Loginmodule(UIModule):
    def render(self):
        # self.request.query uri参数 
        # self.request.path uri路径
        # self.request.uri 路径+参数
        if self.request.query:
            msg = '用户名或密码错误'
        else:
            msg = ''
        return self.render_string('mymodule/login_module.html',msg=msg)


class BlogModule(UIModule):
    def render(self):
        dbutil = DBUtil()
        blogs = dbutil.get_blogs()
        print(blogs)
        return self.render_string('mymodule/blog_module.html',
                                  blogs=blogs)

class CheckHandler(RequestHandler):
    def get(self):
        pass
    
    def post(self):
        uname = self.get_body_argument('uname',None)
        dbutil = DBUtil()
        if dbutil.isexists(uname):
            self.write({'msg':'fail'})
        else:
            self.write({'msg':'ok'})


class CCCHandler(RequestHandler):
    def get(self):
        pass
    
    def post(self):
        uname = self.get_body_argument('uname',None)
        dbutil = DBUtil()
        r = dbutil.avatar(uname)
        self.write({"avatar":r})
