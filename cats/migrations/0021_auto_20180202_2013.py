# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-02 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0020_animalvideo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalvideo',
            name='put_to_index_page',
            field=models.BooleanField(default=True, verbose_name='Поместить на стартовую'),
        ),
        migrations.AlterField(
            model_name='animalvideo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
    ]
