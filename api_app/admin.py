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


class RoleAdmin(admin.ModelAdmin):
    list_display = ['description']
admin.site.register(models.Role, RoleAdmin)

admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
