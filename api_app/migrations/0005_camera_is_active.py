# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-31 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_auto_20170130_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='camera is activated'),
        ),
    ]
