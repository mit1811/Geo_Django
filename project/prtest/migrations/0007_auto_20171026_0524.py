# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prtest', '0006_auto_20171026_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='students_by_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='students_by_teacher',
            field=models.ManyToManyField(related_name='students_by_teacher', to='prtest.Course'),
        ),
    ]
