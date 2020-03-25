from django.forms import ModelForm, forms
from SolarPV import models
from django.contrib.auth.models import User
import io, csv


class ProductRegistration(ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class ManufacturerRegistration(ModelForm):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'


class UserRegistration(ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'


class UserLogin(ModelForm):
    class Meta:
        fields = ['username', 'password']


