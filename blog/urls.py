#encoding=utf8
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
    '',
    url('^$', views.home),
    # 根据页数导航
    # url(r'^(?P<page>\d*)/?$', views.home),
    url(r'^(?P<page>\d*)/?$', views.home),
    url('^archive/$', views.archive),
    url('^about/$', views.about),
    # TODO url 修改
    # url(r'^(?P<id>\d+)/$', views.blogpost, name='blog'),
    # url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/?P<slug>[-\w]+/$', views.blogpost_new),
      url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.blogpost_new),

    # url /blog/category/xx

    # url /blog/tag/xx

)
