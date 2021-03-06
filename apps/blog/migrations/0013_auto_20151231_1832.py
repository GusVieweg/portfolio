# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 18:32
from __future__ import unicode_literals

from django.db import migrations


def change_desc(apps, schema_editor):
    """

    :param apps:
    :param schema_editor:
    :return:
    """
    Post = apps.get_model("blog", "Post")
    p = Post.objects.get(title="Transformations")
    p.description = "Post involving an in depth derivation of the Fourier Transform and particular insights I found important during the process."
    p.title = "Fourier Transform"
    p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151229_1945'),
    ]

    operations = [
        migrations.RunPython(change_desc),
    ]
