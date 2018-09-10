# webapp.py
'''处理特定请求的模块'''
import time

def app(environ, start_response):
    status = '200 OK'
    response_heads = [('Content-Type', 'text/plain;charset=utf-8')]
    start_response(status, response_heads)
    return '\n==简单的app程序==\n%s' % time.ctime()
