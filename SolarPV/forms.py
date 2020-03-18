from django.forms import ModelForm
from . import models


class ProductRegistration(ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class ManufacturerRegistration(ModelForm):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'




















    # manufacturer = forms.CharField(label="Manufacturer", max_length=100)
    # location = forms.CharField(label="Location", max_length=100)
    # contact = forms.CharField(label="Contact", max_length=100)
    # address = forms.CharField(label="Address", max_length=100)
    # email = forms.EmailField(label='Email')
    # phone = forms.CharField(label='Phone')
    # model_number = forms.CharField(max_length=45)
    # manufacturing_date = forms.DateField
    # length = forms.FloatField()
    # width = forms.FloatField()
    # weight = forms.FloatField()
    # cell_area = forms.FloatField()
    # cell_technology = forms.CharField(max_length=50)
    # total_numbers_of_cells = forms.IntegerField()
    # number_of_cells_in_series = forms.IntegerField()
    # number_of_series_strings = forms.IntegerField()
    # number_of_bypass_diodes = forms.IntegerField()
    # series_fuse_rating = forms.FloatField()
    # interconnect_material = forms.CharField(max_length=45)
    # interconnect_supplier = forms.CharField(max_length=45)
    # superstrate_type = forms.CharField(max_length=45)
    # superstrate_manufacturer = forms.CharField(max_length=45)
    # substrate_type = forms.CharField(max_length=45)
    # substrate_manufacturer = forms.CharField(max_length=45)
    # frame_material = forms.CharField(max_length=45)
    # frame_adhesive = forms.CharField(max_length=45)
    # encapsulant_type = forms.CharField(max_length=45)
    # junction_box_type = forms.CharField(max_length=45)
    # junction_box_manufacturer = forms.CharField(max_length=45)
    # cable_type = forms.CharField(max_length=45)
    # connector_type = forms.CharField(max_length=45)
    # maximum_system_voltage = forms.FloatField()
    # rated_voc = forms.FloatField()
    # rated_isc = forms.FloatField()
    # rated_vmp = forms.FloatField()
    # rated_imp = forms.FloatField()
    # rated_pmp = forms.FloatField()
    # rated_ff = forms.FloatField()