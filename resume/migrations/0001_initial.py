# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('employer', models.CharField(max_length=100)),
                ('employer_link', models.URLField()),
                ('date_started', models.DateTimeField()),
                ('date_ended', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'verbose_name': 'Job',
            },
        ),
        migrations.CreateModel(
            name='JobResponsibility',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('job', models.ForeignKey(related_name='responsibilities', to='resume.Job', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Job Responsibilities',
                'verbose_name': 'Job Responsibility',
            },
        ),
        migrations.CreateModel(
            name='ResumeLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Resume Links',
                'verbose_name': 'Resume Link',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=200)),
                ('date_started', models.DateTimeField()),
                ('date_ended', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Schools',
                'verbose_name': 'School',
            },
        ),
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=30)),
                ('value', models.TextField()),
                ('school', models.ForeignKey(related_name='details', to='resume.School', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'School Details',
                'verbose_name': 'School Detail',
            },
        ),
    ]
