# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-23 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('text', models.TextField(blank=True, default='', verbose_name='Текст статьи')),
            ],
        ),
    ]
