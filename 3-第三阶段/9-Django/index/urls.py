from django.conf.urls import url
from .views import *

urlpatterns = [
    # 访问路径　localhost:8000/
    url(r'^$', index_views, name='index'),
    # 访问路径　localhost:8000/login
    url(r'^login/$', login_views, name='login'),
    # 访问路径　localhost:8000/register
    url(r'^register/$', register_views, name='register'),

]
