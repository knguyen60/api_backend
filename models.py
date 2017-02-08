# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
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


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    google_id = models.CharField(max_length=255)
    dropbox_id = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=30)
    email = models.CharField(unique=True, max_length=255)
    api_key = models.CharField(max_length=32)
    goodle_token = models.CharField(max_length=255)
    dropbox_token = models.CharField(max_length=255)
    is_confirmed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='role')

    class Meta:
        managed = False
        db_table = 'user'


class Viewer(models.Model):
    master = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, db_column='permission')
    viewer = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'viewer'
