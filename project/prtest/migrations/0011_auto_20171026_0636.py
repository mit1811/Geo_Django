# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prtest', '0010_auto_20171026_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='students_by_teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='students_by_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prtest.Course'),
        ),
    ]
