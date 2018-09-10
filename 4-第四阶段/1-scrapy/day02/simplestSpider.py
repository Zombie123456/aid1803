# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:54:41 2018

@author: Administrator
"""

# 最简单的爬虫程序
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
from urllib import request
print(request.urlopen(
      request.Request("http://www.sina.com.cn",
                      headers=headers)
      ).read().decode("utf-8")
     )

# TODO:
# ???思考：在requests中如何修改user-agent???
#import requests #Python3
##print(requests.get('http://www.sina.com.cn').text)
#res = requests.get('http://www.sina.com.cn')
#res.encoding = "utf-8"
#print(res.text)

