
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    registered_country = models.TextField(blank=True, null=True)
    contact_person = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    model_number = models.CharField(max_length=45)
    manufacturing_date = models.CharField(unique=True, max_length=8)
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
    manufacturer = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Testlab(models.Model):
    testlab_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    contact_person = models.ForeignKey('User', models.DO_NOTHING, db_column='contact_person', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testlab'


class Testresutls(models.Model):
    testresults_id = models.AutoField(primary_key=True)
    report_condition = models.CharField(max_length=255, blank=True, null=True)
    test_squence = models.CharField(max_length=255, blank=True, null=True)
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
        managed = False
        db_table = 'testresutls'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    office_phone = models.CharField(max_length=15, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
