# Generated by Django 3.1.6 on 2021-04-16 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0018_auto_20210416_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
