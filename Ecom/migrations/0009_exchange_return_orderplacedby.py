# Generated by Django 3.1.7 on 2021-10-05 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecom', '0008_auto_20211005_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange_return',
            name='orderplacedby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orderplacedbyuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
