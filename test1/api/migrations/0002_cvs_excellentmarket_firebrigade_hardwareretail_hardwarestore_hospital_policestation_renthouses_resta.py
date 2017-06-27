# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cvs',
            fields=[
                ('taxid_number', models.CharField(max_length=8, null=True, db_column='TaxID_Number', blank=True)),
                ('company_name', models.CharField(max_length=12, null=True, db_column='Company_Name', blank=True)),
                ('branch_taxid_number', models.CharField(max_length=8, serialize=False, primary_key=True, db_column='Branch_TaxID_Number')),
                ('branch_name', models.CharField(max_length=11, null=True, db_column='Branch_Name', blank=True)),
                ('location', models.CharField(max_length=60, null=True, db_column='Location', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
                ('status', models.CharField(max_length=2, null=True, db_column='Status', blank=True)),
            ],
            options={
                'db_table': '02_CVS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Excellentmarket',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('year', models.CharField(max_length=34, null=True, db_column='Year', blank=True)),
                ('name', models.CharField(max_length=19, null=True, db_column='Name', blank=True)),
                ('location', models.CharField(max_length=25, null=True, db_column='Location', blank=True)),
                ('hours', models.CharField(max_length=10, null=True, db_column='Hours', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
                ('introduction', models.CharField(max_length=1320, null=True, db_column='Introduction', blank=True)),
                ('famousstore', models.CharField(max_length=194, null=True, db_column='FamousStore', blank=True)),
            ],
            options={
                'db_table': '02_ExcellentMarket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Firebrigade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('team', models.CharField(max_length=3, null=True, db_column='Team', blank=True)),
                ('name', models.CharField(max_length=19, null=True, db_column='Name', blank=True)),
                ('location', models.CharField(max_length=33, null=True, db_column='Location', blank=True)),
                ('phone_number', models.CharField(max_length=52, null=True, db_column='Phone_Number', blank=True)),
                ('point_x', models.DecimalField(null=True, decimal_places=4, max_digits=10, db_column='Point_X', blank=True)),
                ('point_y', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column='Point_Y', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '01_FireBrigade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hardwareretail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('taxid_number', models.IntegerField(null=True, db_column='TaxID_Number', blank=True)),
                ('name', models.CharField(max_length=18, null=True, db_column='Name', blank=True)),
                ('location', models.CharField(max_length=49, null=True, db_column='Location', blank=True)),
                ('status', models.CharField(max_length=6, null=True, db_column='Status', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '02_HardwareRetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hardwarestore',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('taxid_number', models.IntegerField(null=True, db_column='TaxID_Number', blank=True)),
                ('name', models.CharField(max_length=18, null=True, db_column='Name', blank=True)),
                ('location', models.CharField(max_length=40, null=True, db_column='Location', blank=True)),
                ('status', models.CharField(max_length=4, null=True, db_column='Status', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '02_HardwareStore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.CharField(max_length=12, serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=24, null=True, db_column='Name', blank=True)),
                ('field_field', models.CharField(max_length=15, null=True, db_column='\u6b0a\u5c6c\u5225', blank=True)),
                ('type', models.CharField(max_length=6, null=True, db_column='Type', blank=True)),
                ('city', models.CharField(max_length=6, null=True, db_column='City', blank=True)),
                ('munber', models.CharField(max_length=36, null=True, db_column='Munber', blank=True)),
                ('location', models.CharField(max_length=134, null=True, db_column='Location', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '01_Hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Policestation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=8, null=True, db_column='Name', blank=True)),
                ('en_name', models.CharField(max_length=33, null=True, db_column='En_Name', blank=True)),
                ('postal_code', models.IntegerField(null=True, db_column='Postal_Code', blank=True)),
                ('location', models.CharField(max_length=21, null=True, db_column='Location', blank=True)),
                ('phone_number', models.CharField(max_length=12, null=True, db_column='Phone_Number', blank=True)),
                ('point_x', models.DecimalField(null=True, decimal_places=4, max_digits=10, db_column='Point_X', blank=True)),
                ('point_y', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column='Point_Y', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '01_PoliceStation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Renthouses',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('area', models.CharField(max_length=2, null=True, db_column='Area', blank=True)),
                ('thingname', models.CharField(max_length=23, null=True, db_column='ThingName', blank=True)),
                ('location', models.CharField(max_length=23, null=True, db_column='Location', blank=True)),
                ('money', models.CharField(max_length=8, null=True, db_column='Money', blank=True)),
                ('landlord', models.CharField(max_length=29, null=True, db_column='LandLord', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
                ('source', models.CharField(max_length=149, null=True, db_column='Source', blank=True)),
            ],
            options={
                'db_table': '00_RentHouses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('taxid_number', models.IntegerField(null=True, db_column='TaxID_Number', blank=True)),
                ('name', models.CharField(max_length=13, null=True, db_column='Name', blank=True)),
                ('location', models.CharField(max_length=69, null=True, db_column='Location', blank=True)),
                ('status', models.CharField(max_length=7, null=True, db_column='Status', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '02_Restaurant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WChild',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('location', models.CharField(max_length=35, null=True, db_column='Location', blank=True)),
                ('police_station', models.CharField(max_length=8, null=True, db_column='Police_Station', blank=True)),
                ('branch_office', models.CharField(max_length=6, null=True, db_column='Branch_Office', blank=True)),
                ('lat', models.FloatField(db_column='Lat')),
                ('lng', models.FloatField(db_column='Lng')),
            ],
            options={
                'db_table': '03_WChild',
                'managed': False,
            },
        ),
    ]
