"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', "web.views.index", name='index'),
    url(r'^upload/$', "web.views.uploadfile", name='upload'),
    url(r'^upload1/$', "web.views.uploadfile1", name='upload1'),
    url(r'^uploadtwitter/$', "web.views.uploadfiletwitter", name='uploadtwitter'),
    url(r'^creation_model/$', "web.views.creationmodel", name='creationmodel'),
    url(r'^creation_convex/$', "web.views.creationconvex", name='creationconvex'),
    url(r'^creation_twitter/(?P<hash1>[\w\-]+)/(?P<hash2>[\w\-]+)/(?P<hash3>[\w\-]+)/$', "web.views.creationtwitter", name='creationtwitter'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
