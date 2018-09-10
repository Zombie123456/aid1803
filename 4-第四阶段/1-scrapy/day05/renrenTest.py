# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:00:47 2018

@author: Python
"""

import urllib

# 这里的URL是每个人自己的主页
url = "http://www.renren.com/961482489/profile"

# header里面需要一个cookie,
#这里的cookie需要你首先登录人人网，
#然后在抓包工具中提取出这个cookie
ua_header = {"Connection":"keep-alive",
             "Cookie":"anonymid=jjnx1d1cihlzuo; depovince=BJ; jebecookies=ebe1816f-5f75-4579-88c0-ad00b7e4c313|||||; _r01_=1; JSESSIONID=abcGVjeDuxBKbgZug4Hsw; ick_login=65bd6e9b-c0b9-420f-9828-5b289e595cfe; jebe_key=55771536-eebf-4500-bbdc-7f20196aa369%7C65617699d9107c4fa92a82edbc369e2a%7C1531724218677%7C1%7C1531724225419; _de=7113E26C6AAF3646A83FD76533146E3C; p=25d6b827f3bb700618db95f447d2c20e9; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=11158b98cbc43eba8b628e5a4cc064049; societyguester=11158b98cbc43eba8b628e5a4cc064049; id=961482489; xnsid=5e1f44f2; loginfrom=syshome; wp_fold=0",
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
             "Host":"www.renren.com"}

req = urllib.request.Request(url, 
                     headers=ua_header)
response = urllib.request.urlopen(req)

with open("myRenren.html", "wb") as f:
    f.write(response.read())



