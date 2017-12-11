# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prtest', '0004_auto_20171025_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_by_teacher',
        ),
        migrations.RemoveField(
            model_name='student',
            name='students_by_course',
        ),
        migrations.AddField(
            model_name='student',
            name='students_by_teacher',
            field=models.ManyToManyField(related_name='students_by_teacher', to='prtest.Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_by_course',
            field=models.ManyToManyField(related_name='teacher_by_course', to='prtest.Course'),
        ),
    ]