# Generated by Django 3.1.7 on 2021-03-16 13:16

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=10)),
                ('id_user', models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('object', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=2000)),
                ('id_user', models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('blocker', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=100)),
                ('id_buyer', models.ForeignKey(on_delete=models.SET('unknown'), to='order.buyer')),
                ('id_user', models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
