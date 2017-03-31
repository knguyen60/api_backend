# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApiAppVideopath(models.Model):
    path = models.CharField(max_length=200)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_app_videopath'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Camera(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    uid = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'camera'


class Deviceendpoint(models.Model):
    endpoint = models.TextField()
    device_data = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'deviceEndpoint'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSesSesstat(models.Model):
    date = models.DateField(unique=True)
    delivery_attempts = models.IntegerField()
    bounces = models.IntegerField()
    complaints = models.IntegerField()
    rejects = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_ses_sesstat'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Notification(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    email_notify = models.IntegerField()
    android_notify = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'


class Notificationdevice(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    type = models.CharField(max_length=10)
    endpoint = models.TextField()
    device_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'notificationDevice'


class Permission(models.Model):
    p_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Schedule(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    is_active = models.IntegerField()
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    time_from = models.TimeField()
    time_to = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule'


class User(models.Model):
    google_id = models.CharField(max_length=255)
    dropbox_id = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=128)
    api_key = models.CharField(max_length=32)
    android_token = models.CharField(max_length=255)
    dropbox_token = models.CharField(max_length=255)
    is_confirmed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    is_viewer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Viewer(models.Model):
    master = models.ForeignKey(User, models.DO_NOTHING)
    viewer = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, db_column='permission')

    class Meta:
        managed = False
        db_table = 'viewer'
