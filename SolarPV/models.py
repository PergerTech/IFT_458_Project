
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phone_field.models import PhoneField

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


class Client(models.Model):
    choices = [('bad', 'bad client'), ('good', 'good client'), ('good client', 'really good client'), ('bad client', 'really bad client')]
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(null=True, blank=True, max_length=100)
    client_type = models.CharField(max_length=30, choices=choices, default='good client')

    def __str__(self):
        return self.client_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    office_phone = PhoneField(blank=True, help_text='Office contact number')
    cell_phone = PhoneField(blank=True, help_text='Cell contact number')
    prefix_choices = [('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Dr', 'Dr')]
    prefix = models.CharField(max_length=4, choices=prefix_choices, default=None)
    company = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Location(models.Model):
    location_id = models.AutoField(primary_key=True, )
    address1 = models.CharField(blank=True, null=True, max_length=100)
    address2 = models.CharField(blank=True, null=True, max_length=100)
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    postal_code = models.CharField(max_length=5, default=77777)
    country = models.CharField(blank=True, null=True, max_length=50)
    phone_number = PhoneField(blank=True, null=True)
    fax_number = PhoneField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, related_name='client')

    def __str__(self):
        return self.address1 + ', ' + self.city + ', ' + self.state

    def __unicode__(self):
        return self.address1 + ', ' + self.city + ', ' + self.state


class Standard(models.Model):
    standard_id = models.AutoField(primary_key=True)
    standard_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    published_date = models.DateField()

    def __str__(self):
        return self.standard_name


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True)
    is_FI_required = models.BooleanField(default=False)
    FI_frequency = models.FloatField(null=True, max_length=10)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.service_id


class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    report_number = models.IntegerField(blank=True, null=True)
    issue_date = models.DateField()
    standard_id = models.ForeignKey(Standard, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.report_number
