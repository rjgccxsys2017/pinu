# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=200, verbose_name='message content'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sended_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
