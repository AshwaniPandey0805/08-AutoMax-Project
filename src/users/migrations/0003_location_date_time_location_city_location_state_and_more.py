# Generated by Django 4.2.2 on 2023-07-16 14:10

from django.db import migrations, models
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
