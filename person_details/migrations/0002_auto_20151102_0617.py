# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Link Type',
                'verbose_name_plural': 'Link Types',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person_details.LinkType', default=None),
            preserve_default=False,
        ),
    ]
