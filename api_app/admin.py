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
    list_display = ['is_active', 'monday', 'tuesday', 'wednesday', 'thursday',
                    'friday', 'saturday', 'sunday', 'time_from', 'time_to',]
admin.site.register(models.Schedule, ScheduleAdmin)

admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
