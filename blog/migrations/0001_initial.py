# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('allowed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'verbose_name': 'Post',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blog.Post', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
