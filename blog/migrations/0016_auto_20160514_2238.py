# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-14 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160514_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='home', on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
