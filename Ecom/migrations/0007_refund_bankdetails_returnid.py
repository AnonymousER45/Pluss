# Generated by Django 3.1.7 on 2021-10-05 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0006_auto_20211005_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund_bankdetails',
            name='returnid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Ecom.exchange_return'),
        ),
    ]
