# Generated by Django 4.0.6 on 2022-07-28 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('mobileNumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=7)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='turfDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turfName', models.CharField(max_length=125)),
                ('mobileNumber', models.CharField(max_length=12)),
                ('openingTime', models.TimeField()),
                ('cloasingTime', models.TimeField()),
                ('addressOfTurf', models.CharField(max_length=255)),
                ('aminities', models.CharField(max_length=225)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.admin')),
            ],
        ),
        migrations.CreateModel(
            name='turfImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generalTurfImages', models.ImageField(blank=True, null=True, upload_to='images')),
                ('turfDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.turfdetails')),
            ],
        ),
    ]
