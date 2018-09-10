from app.myapp import *
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application

define('port',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ('/register',registerHandler),
                            ('/check',CheckHandler),
                            ('/ccc', CCCHandler)],
                  template_path='Mytemplates',
                  static_path='mystatics',
                  ui_modules={'loginmodule':Loginmodule,
                              'blogmodule':BlogModule})
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()
