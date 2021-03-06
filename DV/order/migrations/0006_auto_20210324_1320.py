# Generated by Django 3.1.7 on 2021-03-24 12:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_duration',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL),
        ),

        migrations.AlterField(
            model_name='order',
            name='review',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]




