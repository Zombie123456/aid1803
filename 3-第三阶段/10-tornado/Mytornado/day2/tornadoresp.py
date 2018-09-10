from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler
import json


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
        if username=='abc' and password=='123':
            #如果用户真上传了文件
            #把上传的文件保存到服务器
            #self.request是RequestHandler
            #的一个属性，引用HttpServerReqeust对象
            #该对象中封装了与请求相关的所有内容
            print(self.request)
            #HttpServerRequest对象的files属性
            #引用着用户通过表单上传的文件
            #如果用户没有上传文件，files属性是空字典{}
            #如果上传了文件
            #{'avatar':[{
            # 'content_type':'image/jpeg',
            # 'body':二进制格式表示的图像的内容,
            # 'filename':上传者本地图像名称},
            # {},
            # {}....]}
            print(self.request.files)
            if self.request.files:
                avs = self.request.files['avatar']
                for a in avs:
                    body = a['body']
                    #上传的这一个个文件内容
                    #保存到服务器的硬盘上
                    writer = open('upload/%s'%a['filename'],'wb')
                    writer.write(body)
                    writer.close()
            #跳转到blog页面
            self.redirect('/blog?username='+username)
        else:
            #跳转回登录界面
            self.redirect('/?msg=用户名或密码错误')


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('blog.html',
        blogs=[{
                'author':'旭旭宝宝',
                'title':'dnf',
                'content':'打团摸鱼',
                'tags':'乌龟 卢克',
                'count':55421,
                'avatar':''
            },{
                'author':'大脓包',
                'title':'dnf',
                'content':'打团摸金',
                'tags':'乌龟 卢克 超时空',
                'count':0,
                'avatar':'2.jpg'
            },{
                'author':'五五开',
                'title':'吃鸡 LOL',
                'content':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem aperiam deleniti ullam consectetur veritatis in placeat. Consequuntur sunt ipsa voluptatibus, aliquid, tenetur sequi cumque quisquam, commodi iste temporibus eum nam!',
                'tags':'挂狗 丑逼',
                'count':54231445,
                'avatar':'3.jpg'
                }])

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

 
define('port',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler)],
                  template_path='Mytemplates',
                  static_path='mystatics')
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()
