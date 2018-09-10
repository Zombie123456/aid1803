# gevent0.py
import gevent

def foo(a):
    print('r',a)
    gevent.sleep(2)
    print('s')

def bar():
    print('rb')
    gevent.sleep(3)
    print('sb')

f = gevent.spawn(foo,1)
b = gevent.spawn(bar)

gevent.joinall([f,b])
