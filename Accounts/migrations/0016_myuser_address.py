# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0015_auto_20160409_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
