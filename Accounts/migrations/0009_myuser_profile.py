# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_remove_friendship_friend_each_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
