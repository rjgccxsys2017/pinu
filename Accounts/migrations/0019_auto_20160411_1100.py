# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0018_auto_20160411_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile',
            field=models.ImageField(default='/home/xxx/Desktop/pinu/media/profiles/default_profile.jpg', upload_to='profiles'),
        ),
    ]
