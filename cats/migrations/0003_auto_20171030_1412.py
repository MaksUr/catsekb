# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-30 09:12
from __future__ import unicode_literals

import cats.validators
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_animalimage_background'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldvalue',
            options={'verbose_name': 'Особенность', 'verbose_name_plural': 'Значения особенностей'},
        ),
        migrations.AddField(
            model_name='animalimage',
            name='background_y_position',
            field=models.IntegerField(blank=True, default=50, validators=[cats.validators.background_y_position_validator], verbose_name=django.db.models.fields.IntegerField),
        ),
        migrations.AlterField(
            model_name='animal',
            name='field_value',
            field=models.ManyToManyField(blank=True, default=None, to='cats.FieldValue', verbose_name='Особенность'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='location_status',
            field=models.CharField(blank=True, choices=[('H', 'Пристроен'), ('S', 'Ищут дом'), ('D', 'На радуге')], default='', max_length=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], default='', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='animalimage',
            name='background',
            field=models.BooleanField(default=False, verbose_name='Использовать для фона страницы с котом.'),
        ),
    ]