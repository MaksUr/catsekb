# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-16 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_animal_vk_album_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalimage',
            name='photo_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ID фотографии'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='vk_album_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='ID альбома в VK'),
        ),
    ]
