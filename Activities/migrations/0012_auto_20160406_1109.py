# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 03:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0011_auto_20160406_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='advocator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='advocator', to=settings.AUTH_USER_MODEL),
        ),
    ]
