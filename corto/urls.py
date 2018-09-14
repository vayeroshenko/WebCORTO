from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^button1/$', views.button1, name = 'button1'),
    url(r'^cmount/$', views.cmount, name = 'cmount'),
    url(r'^make/$', views.make, name = 'make'),
    url(r'^makeclean/$', views.makeclean, name = 'makeclean'),
    url(r'^lmount/$', views.lmount, name = 'lmount'),
    url(r'^cunmount/$', views.cunmount, name = 'cunmount'),
    url(r'^lunmount/$', views.lunmount, name = 'lunmount'),
    url(r'^crontabon/$', views.crontabon, name = 'crontabon'),
    url(r'^crontaboff/$', views.crontaboff, name = 'crontaboff'),
    url(r'^convert/$', views.convert, name = 'convert'),
    url(r'^clear/$', views.clear, name = 'clear'),
    url(r'^startrun/$', views.startrun, name = 'startrun'),
    url(r'^stoprun/$', views.stoprun, name = 'stoprun'),
    url(r'^wccheck/$', views.wccheck, name = 'wccheck'),
    url(r'^forcesync/$', views.forcesync, name = 'forcesync'),
    url(r'^forceconv/$', views.forceconv, name = 'forceconv'),
]
