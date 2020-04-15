# Generated by Django 3.0.4 on 2020-04-11 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SolarPV', '0010_auto_20200406_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_type', models.CharField(choices=[('bad', 'bad client'), ('good', 'good client'), ('good client', 'really good client'), ('bad client', 'really bad client')], default='good client', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('standard_id', models.AutoField(primary_key=True, serialize=False)),
                ('standard_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200, null=True)),
                ('is_FI_required', models.BooleanField(default=False)),
                ('FI_frequency', models.FloatField(max_length=10, null=True)),
                ('standard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SolarPV.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('fax_number', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SolarPV.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_number', models.IntegerField(blank=True, null=True)),
                ('issue_date', models.DateField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SolarPV.Location')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SolarPV.Product')),
                ('standard_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SolarPV.Standard')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
