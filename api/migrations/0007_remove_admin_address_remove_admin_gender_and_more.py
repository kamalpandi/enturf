# Generated by Django 4.0.6 on 2022-09-13 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_bookingreport_playersaccount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='address',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='pincode',
        ),
    ]
