# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0002_auto_20180902_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='readers',
        ),
    ]
