from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


# def login_views(request):
#     # 根据用户的请求意图决定该干什么事情
#     if request.method == 'GET':
#         # 1. if cookies contains uid & uphone
#         if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'login.html')
#     else:
#         # 处理用户登录操作
#         uphone = request.POST['uphone']
#         upwd = request.POST['upwd']
#         users = Users.objects.filter(uphone=uphone, upwd=upwd)
#         if users:
#             # 获取用户的ID
#             uid = users[0].id
#             # 创建 重定向响应对象
#             resp = HttpResponseRedirect('/')
#             # 判断是否记住密码
#             if 'isSaved' in request.POST:
#                 # 将用户ID以及手机号保存进cookie
#                 expires = 60 * 60 * 24 * 366
#                 resp.set_cookie('uid', uid, expires)
#                 resp.set_cookie('uphone', uphone, expires)
#             # 将响应对象响应给客户端
#             return resp

#             # return HttpResponseRedirect('/')
#         else:
#             errMsg = '用户名或密码不正确'
#             return render(request, 'login.html', locals())


def index_views(request):
    return render(request, 'index.html')


def register_views(request):
    # return render(request, 'register.html')
    # 根据用户的请求意图决定到底该做什么操作
    # 如　：get　请求，查看注册页面
    # 如　：post　请求，处理提交数据(注册)

    if request.method == 'GET':
        return render(request, 'register.html',errmsg='')
    else:
        uphone = request.POST['uphone']
        # 判断uphone在数据库中是否存在
        users = Users.objects.filter(uphone=uphone)
        if users:
            # 说明用户已经存在
            errMsg = '电话号码已存在，请重新输入'
            return render(request, 'register.html', locals())
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        Users.objects.create(uphone=uphone, upwd=upwd,
                             uname=uname, uemail=uemail)
        return HttpResponseRedirect('/login/')


def login_views(request):
    # 判断是post 请求还是 get 请求
    if request.method == 'POST':
        # 实现登录操作
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        users = Users.objects.filter(uphone=uphone, upwd=upwd)
        if users:
            # 登录成功
            # 将登录信息保存进session
            request.session['id'] = users[0].id
            request.session['uphone'] = uphone
            # 创建响应对象
            resp = HttpResponseRedirect('/')
            # 判断是否要保存进 cookies
            if 'isSaved' in request.POST:
                # 需要保存进 cookies
                expires = 60 * 60 * 24 * 366
                resp.set_cookie('id', users[0].id, expires)
                resp.set_cookie('uphone', uphone, expires)
            return resp
        else:
            # 登录失败
            errMsg = '用户名或密码不正确'
            return render(request, 'login.html', locals())
    else:
        # GET 请求
        # 判断 session 中是否有登录信息
        if 'id' in request.session and 'uphone' in request.session:
            # 重定向到首页
            return HttpResponseRedirect('/')
        else:
            # session 中没有登录信息
            # 判断 cookie 是否包含登录信息
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                # cookies 中包含登录信息
                # 从cookies中获取登录信息并保存进session中
                id = request.COOKIES['id']
                uphone = request.COOKIES['uphone']
                request.session['id'] = id
                request.session['uphone'] = uphone
                return HttpResponseRedirect('/')
            else:
                # cookies 中不包含登录信息
                return render(request, 'login.html')
