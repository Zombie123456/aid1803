# http_server.py
try:
    from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler,HTTPServer

class RequestHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        # print(self.rfile.read(1024)) 请求体
        f = open('test.html','rb')
        content = f.read()
        self.send_response(200)
        self.send_header('asd','text/html')
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        pass


ADDR = ('0.0.0.0',8080)
server = HTTPServer(ADDR,RequestHandle)
server.serve_forever()
