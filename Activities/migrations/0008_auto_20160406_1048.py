# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Activities', '0007_remove_activity_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='advocator',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='advocator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='person_joined',
            field=models.ManyToManyField(blank=True, default=None, related_name='person_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
