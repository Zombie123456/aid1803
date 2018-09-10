from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def request_views(request):
    # print(dir(request))
    # return HttpResponse('OK')
    scheme = request.scheme
    body = request.body
    path = request.path
    method = request.method
    get = request.GET
    host = request.get_host()
    post = request.POST
    cookies = request.COOKIES
    return render(request, '01_request.html', locals())

def login_views(request):
    if request.method == 'GET':
        return render(request, '02_login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse(uname + upwd)
