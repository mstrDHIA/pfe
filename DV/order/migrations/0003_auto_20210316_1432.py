# Generated by Django 3.1.7 on 2021-03-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210316_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='lat',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='long',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
