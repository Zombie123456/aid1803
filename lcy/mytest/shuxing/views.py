from django.shortcuts import render

# Create your views here.
from shuxing.models import Zb_type


def find_type():
    ty = Zb_type.objects.all()
    return ty




def index_views(request):
    tys = find_type()
    print(tys)
    return render(request,'shuxing.html',locals())