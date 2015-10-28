# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20151019_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltype',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
