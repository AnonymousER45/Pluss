# Generated by Django 3.1.7 on 2021-10-10 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0008_auto_20210927_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='is_binding',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ecomorder',
            name='date_of_delivery',
            field=models.DateField(default=datetime.date(2021, 10, 15)),
        ),
    ]
