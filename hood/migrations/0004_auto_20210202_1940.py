# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-02 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20210201_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile_pic'),
        ),
    ]
