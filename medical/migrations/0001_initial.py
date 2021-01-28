# Generated by Django 3.1.5 on 2021-01-27 17:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2021, 1, 27, 17, 36, 53, 381357, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(default='', max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('on_medication', models.BooleanField(default=False)),
                ('occupation', models.CharField(default='', max_length=100)),
                ('address', models.TextField(default='')),
                ('emergency_contact_name', models.CharField(max_length=100)),
                ('emergency_contact_number', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None)),
                ('relationship_to_patient', models.CharField(default='', max_length=200)),
                ('medical_implants', models.BooleanField(default=False)),
                ('date_added', models.DateField(default=datetime.datetime(2021, 1, 27, 17, 36, 53, 381357, tzinfo=utc))),
                ('previous_surgery', models.TextField(default='')),
                ('previous_hospitalized', models.TextField(default='')),
                ('registered', models.BooleanField(default=False)),
                ('diseases', models.ManyToManyField(to='medical.Disease')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=200)),
                ('date_created', models.DateField(default=datetime.datetime(2021, 1, 27, 17, 36, 53, 381357, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
