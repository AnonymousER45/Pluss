# Generated by Django 3.1.7 on 2021-08-22 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0002_auto_20210822_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecomorder',
            name='date_of_delivery',
            field=models.DateField(default=datetime.date(2021, 8, 27)),
        ),
    ]
