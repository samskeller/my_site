# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20151011_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=64)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Skill Type',
                'verbose_name_plural': 'Skill Types',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.ForeignKey(related_name='skills', on_delete=django.db.models.deletion.PROTECT, to='resume.SkillType'),
        ),
    ]
