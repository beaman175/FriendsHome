from django.conf.urls import url
from . import views

urlpatterns = [
    #캐럿은 빈경로를 의미
    url(r'^$', views.index),
]
