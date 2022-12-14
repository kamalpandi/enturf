# Generated by Django 4.0.6 on 2022-09-09 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_alter_grounddetails_defaultprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingId', models.CharField(max_length=254, unique=True)),
                ('bookedAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('bookingStatus', models.CharField(choices=[('C', 'NOADVANCE'), ('CL', 'CANCELED'), ('P', 'PENDING')], default='P', max_length=2)),
                ('groundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ground_detailid', to='api.grounddetails')),
            ],
        ),
        migrations.CreateModel(
            name='PlayersAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=125, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='mobileNumber',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='turfdetails',
            name='mobileNumber',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.CreateModel(
            name='PaymentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=125)),
                ('paymentId', models.CharField(max_length=254, unique=True)),
                ('paymentMethod', models.CharField(choices=[('FP', 'FULLPAYMENT'), ('A', 'ADVANCE'), ('NA', 'NOADVANCE')], default='A', max_length=2)),
                ('paymentStatus', models.CharField(choices=[('P', 'PENDING'), ('A', 'ADVANCE'), ('C', 'COMPLETED')], default='P', max_length=2)),
                ('Status', models.BooleanField(default=False)),
                ('playerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_userid', to='api.playersaccount')),
            ],
        ),
        migrations.CreateModel(
            name='CanceledReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancellationId', models.CharField(max_length=254, unique=True)),
                ('cancellationStatus', models.BooleanField(default=False)),
                ('cancellationDate', models.DateTimeField(auto_now_add=True)),
                ('cancellationFee', models.CharField(max_length=100)),
                ('refund', models.CharField(max_length=100)),
                ('bookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookinid_cancel', to='api.bookingreport')),
                ('paymentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentid_cancel', to='api.paymentreport')),
                ('playerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancel_report', to='api.playersaccount')),
            ],
        ),
        migrations.AddField(
            model_name='bookingreport',
            name='paymentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentid_report', to='api.paymentreport'),
        ),
        migrations.AddField(
            model_name='bookingreport',
            name='playerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_userid', to='api.playersaccount'),
        ),
        migrations.AddField(
            model_name='bookingreport',
            name='turfId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turf_detailid', to='api.turfdetails'),
        ),
        migrations.CreateModel(
            name='AdminSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv', models.IntegerField()),
                ('bufferTime', models.TimeField()),
                ('paymentMethod', models.CharField(choices=[('FP', 'FULLPAYMENT'), ('A', 'ADVANCE'), ('NA', 'NOADVANCE')], default='A', max_length=2)),
                ('groundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ground_setting', to='api.grounddetails')),
                ('turfId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turf_setting', to='api.turfdetails')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_setting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
