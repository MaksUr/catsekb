# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-29 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0011_animal_valid_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldvalue',
            name='field_type',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='field_value',
        ),
        migrations.AlterField(
            model_name='animal',
            name='birthday_precision',
            field=models.CharField(choices=[('Y', 'до года'), ('M', 'до месяца'), ('D', 'до дня')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='tag',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Тэг животного'),
        ),
        migrations.DeleteModel(
            name='FieldType',
        ),
        migrations.DeleteModel(
            name='FieldValue',
        ),
    ]
