# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

user = settings.AUTH_USER_MODEL


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(unique=True, max_length=50)
    registered_country = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        
        db_table = 'manufacturer'

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    model_number = models.CharField(max_length=45, unique=True)
    manufacturing_date = models.CharField(unique=False, max_length=8)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    cell_area = models.FloatField(blank=True, null=True)
    cell_technology = models.CharField(max_length=50, blank=True, null=True)
    total_numbers_of_cells = models.IntegerField(blank=True, null=True)
    number_of_cells_in_series = models.IntegerField(blank=True, null=True)
    number_of_series_strings = models.IntegerField(blank=True, null=True)
    number_of_bypass_diodes = models.IntegerField(blank=True, null=True)
    series_fuse_rating = models.FloatField(blank=True, null=True)
    interconnect_material = models.CharField(max_length=45, blank=True, null=True)
    interconnect_supplier = models.CharField(max_length=45, blank=True, null=True)
    superstrate_type = models.CharField(max_length=45, blank=True, null=True)
    superstrate_manufacturer = models.CharField(max_length=45, blank=True, null=True)
    substrate_type = models.CharField(max_length=45, blank=True, null=True)
    substrate_manufacturer = models.CharField(max_length=45, blank=True, null=True)
    frame_material = models.CharField(max_length=45, blank=True, null=True)
    frame_adhesive = models.CharField(max_length=45, blank=True, null=True)
    encapsulant_type = models.CharField(max_length=45, blank=True, null=True)
    junction_box_type = models.CharField(max_length=45, blank=True, null=True)
    junction_box_manufacturer = models.CharField(max_length=45, blank=True, null=True)
    cable_type = models.CharField(max_length=45, blank=True, null=True)
    connector_type = models.CharField(max_length=45, blank=True, null=True)
    maximum_system_voltage = models.FloatField(blank=True, null=True)
    rated_voc = models.FloatField(blank=True, null=True)
    rated_isc = models.FloatField(blank=True, null=True)
    rated_vmp = models.FloatField(blank=True, null=True)
    rated_imp = models.FloatField(blank=True, null=True)
    rated_pmp = models.FloatField(blank=True, null=True)
    rated_ff = models.FloatField(blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.DO_NOTHING,  default=1)

    class Meta:
        
        db_table = 'product'

    def __str__(self):
        return self.model_number


class Testlab(models.Model):
    testlab_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    contact_person = models.ForeignKey(User, models.DO_NOTHING, db_column='contact_person', blank=True, null=True)

    class Meta:
        
        db_table = 'testlab'

    def __str__(self):
        return self.name


class Testresults(models.Model):
    testresults_id = models.AutoField(primary_key=True)
    report_condition = models.CharField(max_length=255, blank=True, null=True)
    test_sequence = models.CharField(max_length=255, blank=True, null=True)
    test_date = models.DateField(blank=True, null=True)
    isc = models.FloatField(blank=True, null=True)
    voc = models.FloatField(blank=True, null=True)
    imp = models.FloatField(blank=True, null=True)
    vmp = models.FloatField(blank=True, null=True)
    pmp = models.FloatField(blank=True, null=True)
    ff = models.FloatField(blank=True, null=True)
    noct = models.FloatField(blank=True, null=True)
    data_source = models.ForeignKey(Testlab, models.DO_NOTHING, db_column='data_source', blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product', blank=True, null=True)

    class Meta:
        
        db_table = 'testresutls'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    office_phone = models.CharField(max_length=15, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
