# Generated by Django 3.1.7 on 2021-07-21 10:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0015_auto_20210709_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('NA', 'Not Available'), ('HD', 'Half Day')], default='NA', max_length=2)),
                ('entry_time', models.DateTimeField(default=datetime.datetime.now)),
                ('exit_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('emp_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
