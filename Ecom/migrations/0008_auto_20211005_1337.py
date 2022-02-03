# Generated by Django 3.1.7 on 2021-10-05 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0007_refund_bankdetails_returnid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund_bankdetails',
            name='return_id',
        ),
        migrations.RemoveField(
            model_name='refund_upidetails',
            name='return_id',
        ),
        migrations.AddField(
            model_name='refund_upidetails',
            name='returnid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Ecom.exchange_return'),
        ),
    ]
