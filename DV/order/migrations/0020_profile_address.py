# Generated by Django 3.1.6 on 2021-04-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20210416_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
