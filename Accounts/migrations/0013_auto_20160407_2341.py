# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_auto_20160401_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='real_name',
            field=models.CharField(max_length=100),
        ),
    ]
