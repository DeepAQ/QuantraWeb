# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0004_remove_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]