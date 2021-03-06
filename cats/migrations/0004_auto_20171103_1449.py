# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-03 09:49
from __future__ import unicode_literals

import cats.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20171030_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalimage',
            name='alt',
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='background_y_position',
            field=models.IntegerField(blank=True, default=50, validators=[cats.validators.background_y_position_validator], verbose_name='Настройка позиции фонового изображения по вертикали.'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=100, verbose_name='Описание'),
        ),
    ]
