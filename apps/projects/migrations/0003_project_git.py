# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151219_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.URLField(default='https://github.com/jrpotter/', max_length=255),
            preserve_default=False,
        ),
    ]
