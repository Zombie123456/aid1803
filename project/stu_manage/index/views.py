from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from io import BytesIO
from PIL import ImageFont,Image,ImageDraw
import random
from utils.check_code import create_validate_code
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        pass

def index(request):
    return render(request, 'index.html')

def yz_home(requset):
    if requset.method=='GET':
        return render(requset,'yz_home.html')
    else:
        return HttpResponse('ok')

def yanzheng(requset):
    f=BytesIO()
    img,code=create_validate_code()
    requset.session['check_code']=code
    img.save(f,'PNG')
    return HttpResponse(f.getvalue())

