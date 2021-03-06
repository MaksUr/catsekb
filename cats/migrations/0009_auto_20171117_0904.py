# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-17 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0008_auto_20171116_1014'),
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
        migrations.AddField(
            model_name='animalimage',
            name='image_small_url',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='URL сжатого изображения'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='image_url',
            field=models.URLField(verbose_name='URL изображения'),
        ),
    ]
