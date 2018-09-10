from urllib import request
print(request.urlopen(
    request.Request('http://www.sina.com.cn').read().decode('utf-8'))
