from django.conf.urls import url, include
from django.contrib import admin
from api_app import views
import djoser.views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    # url(r'^register/$', views.UserRegister.as_view(), name='register'),
    # url(r'^auth/', include('djoser.urls'))
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^profile/(?P<pk>[0-9]+)$', views.UserProfile.as_view(), name='profile'),
    url(r'^androidtoken/(?P<pk>[0-9]+)/$', views.NotificationDevice.as_view(), name='android_token'),
    url(r'^camera/$', views.CameraList.as_view(), name='role'),
    # url(r'^camera/$', views.CameraListByUser.as_view(), name='role'),
    url(r'^camera/(?P<pk>[0-9]+)/$', views.CameraDetail.as_view(), name='camera_detail'),
    url(r'^schedule/create/$', views.ScheduleCreate.as_view(), name='schedule_create'),
    url(r'^schedule/detail/(?P<user__username>[\w.@+-]+)/$', views.ScheduleDetail.as_view(), name='schedule_detail'),
    url(r'^schedule/signal/(?P<user__username>[\w.@+-]+)/$', views.ScheduleSignal.as_view(), name='schedule_signal'),
    url(r'^notification/update/(?P<user__username>[\w.@+-]+)/$', views.NotificationDetail.as_view(), name='notification'),
    url(r'^endpoint/create/$', views.DeviceCreate.as_view(), name='endpoint_create'),
    url(r'^endpoint/detail/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view(), name='android_token'),
    url(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view(), name='role_detail'),
    url(r'^role/$', views.RoleList.as_view(), name='role'),
    url(r'^auth/token/', obtain_jwt_token),
    url(r'^auth/token/refresh/', refresh_jwt_token),
    url(r'^auth/token/verify/', verify_jwt_token)
]
# urlpatterns =[
    
# ]