# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0004_auto_20180902_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookreview.Book'),
        ),
    ]
