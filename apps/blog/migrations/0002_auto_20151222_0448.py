# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_src',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
