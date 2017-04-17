from django.contrib import admin
# Register your models here.
from api_app import models
from django_ses.views import dashboard


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_active']
admin.site.register(models.User, UserAdmin)


class CameraAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'uid']
admin.site.register(models.Camera, CameraAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'monday', 'tuesday', 'wednesday', 'thursday',
                    'friday', 'saturday', 'sunday', 'time_from', 'time_to',]
admin.site.register(models.Schedule, ScheduleAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'endpoint', 'device_data']
admin.site.register(models.NotificationDevice, DeviceAdmin)


class VideoPathAdmin(admin.ModelAdmin):
    list_display = ['video_name','created_time']
admin.site.register(models.VideoPath, VideoPathAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_notify', 'android_notify']
admin.site.register(models.Notification, NotificationAdmin)

admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
