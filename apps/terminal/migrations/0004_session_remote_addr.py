# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0003_auto_20171230_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='remote_addr',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Remote addr'),
        ),
    ]