# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-09 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_auto_20171109_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='vk_album_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ID альбома ВК'),
        ),
    ]
