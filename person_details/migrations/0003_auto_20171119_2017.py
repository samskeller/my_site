# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_details', '0002_auto_20151102_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('detail_type', models.CharField(max_length=40, unique=True)),
                ('detail_value', models.TextField()),
            ],
            options={
                'verbose_name': 'Person Detail',
                'verbose_name_plural': 'Person Details',
            },
        ),
        migrations.AlterField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(related_name='links', on_delete=django.db.models.deletion.PROTECT, to='person_details.LinkType'),
        ),
    ]
