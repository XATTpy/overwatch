from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('highlights/(?P<hero_id>\d+)/$', views.show),
    url('showOne/(?P<video_id>\d+)/$', views.ShowOne),
    url('addcomment/(?P<video_id>\d+)/$', views.addcomment),
    url('sign/', views.sign),
    url('in/', views.inn),
    url('out/', views.out),
    url('addliketovideo/(?P<video_id>\d+)/$', views.addliketovideo),
    url('addliketocomment/(?P<comment_id>\d+)/$', views.addliketocomment),
]
