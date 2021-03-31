# Generated by Django 3.1.7 on 2021-03-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_order_accept_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_duration',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_durations',
            field=models.FloatField(null=True),
        ),
    ]