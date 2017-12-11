# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prtest', '0005_auto_20171026_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='students_by_teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='students_by_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students_by_teacher', to='prtest.Course'),
        ),
    ]
