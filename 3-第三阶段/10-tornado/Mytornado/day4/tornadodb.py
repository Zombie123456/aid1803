import json
import pymysql
import time
import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule
from day4.util.myutil import mymd5


settings = {
    'port':3306,
    'host':'localhost',
    'database':'db_blog',
    'user':'root',
    'password':'123456',
    'charset':'utf8'
}
connection = pymysql.connect(**settings)
cursor = connection.cursor()

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
        sql = 'select user_name from tb_user where user_name = %s \
               and user_password = %s' 
        password = mymd5(password)
        params = (username, password)
        num = cursor.execute(sql, params)
        # result = cursor.fetchone()
        if num:
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
            sql = 'insert into tb_user\
            (user_name,user_password,user_avatar,user_city)\
            values(%s,%s,%s,%s)'
            upwd = mymd5(upwd)
            params2 = (uname,upwd,avatar,ucity)
            try:
                cursor.execute(sql, params2)
                # connection.commit()
                cursor.connection.commit()
            except Exception:
                if avatar:
                    os.remove('mystatics/images/%s' % avatar)
                self.redirect('/register?msg=用户名已存在')
            else:
                self.redirect('/')
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
        sql = 'select user_name,user_avatar,blog_title,tc,c,blog_content from (select comment_blog_id,count(*)c from tb_comment group by comment_blog_id)t3 right join (select user_name,user_avatar,blog_id,blog_title,tc,blog_content from tb_user join (select blog_id,blog_title,tc,blog_user_id,blog_content from tb_blog left join (select rel_blog_id, group_concat(tag_content)tc from tb_tag join (select rel_blog_id,rel_tag_id from tb_blog_tag)t on tag_id = rel_tag_id group by rel_blog_id)t1 on blog_id = rel_blog_id)t2 on user_id = blog_user_id)t4 on comment_blog_id = blog_id;'
        cursor.execute(sql)
        blogss = cursor.fetchall()
        blogs = []
        for i in blogss:
            dit = {
                'author':i[0],
                'title':i[2],
                'content':i[5],
                'tags':i[3],
                'count':i[4],
                'avatar':i[1]
            }
            blogs += dit
        return self.render_string('mymodule/blog_module.html',blogs=blogs)


define('port',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ('/register',registerHandler)],
                  template_path='Mytemplates',
                  static_path='mystatics',
                  ui_modules={'loginmodule':Loginmodule,
                              'blogmodule':BlogModule})
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()
