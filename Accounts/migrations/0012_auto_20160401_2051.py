# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_auto_20160401_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='o2s',
            new_name='friend_each_other',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='s2o',
        ),
    ]
