# Generated by Django 4.0.6 on 2022-07-28 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_admin_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]