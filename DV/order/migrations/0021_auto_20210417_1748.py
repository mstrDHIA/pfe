# Generated by Django 3.1.6 on 2021-04-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='vehicle',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
