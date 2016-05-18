# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro_length',
            field=models.IntegerField(default=0),
        ),
    ]
