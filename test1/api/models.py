# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Hauntedhouse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=2, blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=26, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=23, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '00_HauntedHouse'


class Renthouses(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=2, blank=True, null=True)  # Field name made lowercase.
    thingname = models.CharField(db_column='ThingName', max_length=23, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=23, blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(db_column='Money', max_length=8, blank=True, null=True)  # Field name made lowercase.
    landlord = models.CharField(db_column='LandLord', max_length=29, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=149, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '00_RentHouses'


class Firebrigade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=19, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=33, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=52, blank=True, null=True)  # Field name made lowercase.
    point_x = models.DecimalField(db_column='Point_X', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    point_y = models.DecimalField(db_column='Point_Y', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '01_FireBrigade'


class Hospital(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=12)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=24, blank=True, null=True)  # Field name made lowercase.
    field_field = models.CharField(db_column='\u6b0a\u5c6c\u5225', max_length=15, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    type = models.CharField(db_column='Type', max_length=6, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=6, blank=True, null=True)  # Field name made lowercase.
    munber = models.CharField(db_column='Munber', max_length=36, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=134, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '01_Hospital'


class Policestation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=8, blank=True, null=True)  # Field name made lowercase.
    en_name = models.CharField(db_column='En_Name', max_length=33, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.IntegerField(db_column='Postal_Code', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=21, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=12, blank=True, null=True)  # Field name made lowercase.
    point_x = models.DecimalField(db_column='Point_X', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    point_y = models.DecimalField(db_column='Point_Y', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '01_PoliceStation'


class Cvs(models.Model):
    taxid_number = models.CharField(db_column='TaxID_Number', max_length=8, blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=12, blank=True, null=True)  # Field name made lowercase.
    branch_taxid_number = models.CharField(db_column='Branch_TaxID_Number', primary_key=True, max_length=8)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=11, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '02_CVS'


class Excellentmarket(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=34, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=19, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hours = models.CharField(db_column='Hours', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=1320, blank=True, null=True)  # Field name made lowercase.
    famousstore = models.CharField(db_column='FamousStore', max_length=194, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '02_ExcellentMarket'


class Hardwareretail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taxid_number = models.IntegerField(db_column='TaxID_Number', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=49, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '02_HardwareRetail'


class Hardwarestore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taxid_number = models.IntegerField(db_column='TaxID_Number', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '02_HardwareStore'


class Restaurant(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taxid_number = models.IntegerField(db_column='TaxID_Number', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=13, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=69, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=7, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '02_Restaurant'


class WChild(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=35, blank=True, null=True)  # Field name made lowercase.
    police_station = models.CharField(db_column='Police_Station', max_length=8, blank=True, null=True)  # Field name made lowercase.
    branch_office = models.CharField(db_column='Branch_Office', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat')  # Field name made lowercase.
    lng = models.FloatField(db_column='Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '03_WChild'
