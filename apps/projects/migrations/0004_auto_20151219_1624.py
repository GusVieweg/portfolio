# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 16:24
from __future__ import unicode_literals

from django.db import migrations

def import_git(apps, schema_editor):
    """
    Load up initial applications
    :param apps:
    :param schema_editor:
    :return:
    """
    Project = apps.get_model("projects", "Project")

    appetite = Project.objects.get(title="Appetite")
    appetite.git = "https://github.com/jrpotter/appetite"
    appetite.save()

    portfolio = Project.objects.get(title="Portfolio")
    portfolio.git = "https://github.com/jrpotter/portfolio"
    portfolio.save()

    infection = Project.objects.get(title="Infection")
    infection.git = "https://github.com/jrpotter/infection"
    infection.save()

    huffman = Project.objects.get(title="Huffman Encoding")
    huffman.git = "https://github.com/jrpotter/huffman-encoding"
    huffman.save()

    fifth = Project.objects.get(title="Fifth CAM")
    fifth.git = "https://github.com/jrpotter/fifth"
    fifth.save()

    lodestar = Project.objects.get(title="Lodestar")
    lodestar.git = "https://github.com/jrpotter/lodestar"
    lodestar.save()

    mingle = Project.objects.get(title="Mingle")
    mingle.git = "https://github.com/jrpotter/mingle"
    mingle.save()



class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_git'),
    ]

    operations = [
        migrations.RunPython(import_git),
    ]
