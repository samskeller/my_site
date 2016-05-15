# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('reference', models.CharField(max_length=100)),
                ('post', models.ForeignKey(related_name='images', on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
            options={
                'verbose_name_plural': 'Post Images',
                'verbose_name': 'Post Image',
            },
        ),
    ]
