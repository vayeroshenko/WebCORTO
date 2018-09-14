"""WebCorto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('corto.urls')),
    url(r'^button1/', include('corto.urls')), 
    url(r'^cunmount/', include('corto.urls')), 
    url(r'^lunmount/', include('corto.urls')),
    url(r'^cmount/', include('corto.urls')),
    url(r'^lmount/', include('corto.urls')),
    url(r'^make/', include('corto.urls')),
    url(r'^makeclean/', include('corto.urls')),
    url(r'^crontabon/', include('corto.urls')),
    url(r'^crontaboff/', include('corto.urls')),
    url(r'^convert/', include('corto.urls')),
    url(r'^clear/', include('corto.urls')),
    url(r'^startrun/', include('corto.urls')), 
    url(r'^stoprun/', include('corto.urls')), 
    url(r'^/wccheck/', include('corto.urls')), 
    url(r'^/forcesync/', include('corto.urls')), 
    url(r'^/forceconv/', include('corto.urls')), 
    url(r'^admin/', admin.site.urls),
]
