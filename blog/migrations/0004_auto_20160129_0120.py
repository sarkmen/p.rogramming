# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160129_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, max_length=20, upload_to=''),
        ),
    ]
