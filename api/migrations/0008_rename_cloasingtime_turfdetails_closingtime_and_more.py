# Generated by Django 4.0.6 on 2022-09-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_admin_address_remove_admin_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turfdetails',
            old_name='cloasingTime',
            new_name='closingTime',
        ),
        migrations.AddField(
            model_name='groundpricing',
            name='day',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
