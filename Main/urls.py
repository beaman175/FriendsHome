from django.conf.urls import url
from . import views


app_name = 'Main'
urlpatterns = [
    #캐럿은 빈경로를 의미
    url(r'^$', views.index, name = 'Friends Home'),
    url(r'^house/detail/(?P<id>\d+)/$', views.detail),
    url(r'^house/write/$', views.write, name='write')
    #url(r'^house/detail/(?P<poll_id>\d+)/$', views.detail),

]
