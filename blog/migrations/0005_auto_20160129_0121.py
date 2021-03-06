# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 01:21
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160129_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=blog.models.PhoneField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
