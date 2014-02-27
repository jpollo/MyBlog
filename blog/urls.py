from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
    '',
    url('^$', views.home),
    url('^archive/$', views.archive),
    url('^about/$', views.about),

)
