# Generated by Django 3.1.7 on 2021-10-10 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0011_auto_20211005_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange_return',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='ecomorder',
            name='date_of_delivery',
            field=models.DateField(default=datetime.date(2021, 10, 15)),
        ),
    ]
