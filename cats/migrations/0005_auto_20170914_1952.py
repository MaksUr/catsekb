# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-14 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_animal_birthday_precision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Показывать котика'),
        ),
        migrations.AlterField(
            model_name='group',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Показывать группу'),
        ),
    ]
