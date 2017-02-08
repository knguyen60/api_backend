"""api_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from api_app import urls
from api_app.routes import api_router
from api_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api_app.urls')),
    # url(r'^api/register/$', views.UserRegister.as_view(), name='user'),
    # url(r'^api/camera/$', views.CameraList.as_view(), name='role'),
    # url(r'^api/camera/(?P<pk>[0-9]+)/$', views.CameraDetail.as_view(), name='role_detail'),
    # url(r'^api/role/$', views.RoleList.as_view(), name='role'),
    # url(r'^api/role/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view(), name='role_detail'),
]
