# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-19 09:12
from __future__ import unicode_literals

import cats.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0015_auto_20171213_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalimage',
            name='background',
            field=models.BooleanField(default=False, verbose_name='Использовать для фона страницы.'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='background_y_position',
            field=models.IntegerField(blank=True, default=50, validators=[cats.validators.background_y_position_validator], verbose_name='Позиция по вертикали'),
        ),
    ]
