# Generated by Django 3.1.7 on 2021-06-08 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=None),
        ),
    ]
