# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 01:12
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160127_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone',
            field=blog.models.PhoneField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 100자 이내로 써주세요.', max_length=100, validators=[blog.models.min_length_validator]),
        ),
    ]
