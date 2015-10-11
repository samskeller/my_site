# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_ended',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='date_ended',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
