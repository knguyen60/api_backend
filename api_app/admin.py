from django.contrib import admin
# Register your models here.
from api_app import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email']
admin.site.register(models.User, UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ['description']
admin.site.register(models.Role, RoleAdmin)

