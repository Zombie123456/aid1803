from django.conf.urls import url

from shuxing.views import index_views

urlpatterns = [
    url(r'^index',index_views)
]