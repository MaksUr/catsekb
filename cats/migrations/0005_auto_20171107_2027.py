# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-07 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_auto_20171103_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalimage',
            name='height',
        ),
        migrations.RemoveField(
            model_name='animalimage',
            name='width',
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image_url',
            field=models.ImageField(upload_to='', verbose_name='URL изображения'),
        ),
    ]
