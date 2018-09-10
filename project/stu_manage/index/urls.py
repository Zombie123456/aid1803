from django.conf.urls import url
from .views import login,index,yanzheng,yz_home

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^index/$', index, name='index'),
    url(r'^yzhome.html',yz_home ),
    url(r'^yanzheng.html',yanzheng ),
]