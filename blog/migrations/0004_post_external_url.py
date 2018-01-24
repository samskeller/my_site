# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_intro_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='external_url',
            field=models.URLField(default=''),
        ),
    ]
