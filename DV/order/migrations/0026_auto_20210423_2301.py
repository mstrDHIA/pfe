# Generated by Django 3.1.6 on 2021-04-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20210423_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profits',
            field=models.FloatField(max_length=12, null=True),
        ),
    ]
