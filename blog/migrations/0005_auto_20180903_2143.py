# Generated by Django 2.1.1 on 2018-09-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_external_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='external_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
