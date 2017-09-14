# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-14 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20170913_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1, verbose_name='Пол'),
            preserve_default=False,
        ),
    ]
