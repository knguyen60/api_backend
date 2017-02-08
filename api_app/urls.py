from django.conf.urls import url
from django.contrib import admin
from api_app import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^register/$', views.UserRegister.as_view(), name='register'),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^profile/(?P<pk>[0-9]+)$', views.UserProfile.as_view(), name='profile'),
    url(r'^camera/$', views.CameraList.as_view(), name='role'),
    url(r'^camera/(?P<pk>[0-9]+)/$', views.CameraDetail.as_view(), name='role_detail'),
    url(r'^role/$', views.RoleList.as_view(), name='role'),
    url(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view(), name='role_detail'),
    url(r'^auth/token/', obtain_jwt_token),

]
# urlpatterns =[
    
# ]