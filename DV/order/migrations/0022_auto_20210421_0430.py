# Generated by Django 3.1.6 on 2021-04-21 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20210417_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
