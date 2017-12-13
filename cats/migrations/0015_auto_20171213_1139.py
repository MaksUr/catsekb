# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-13 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0014_auto_20171204_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлено'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='created',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='создано'),
        ),
    ]
