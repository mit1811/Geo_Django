# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20171202_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='recuiter',
            name='search',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
