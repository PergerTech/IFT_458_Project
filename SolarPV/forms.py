from django.forms import ModelForm
from SolarPV import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ProductRegistration(ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class ManufacturerRegistration(ModelForm):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'


# UserForm & ProfileForm are tied together to create an extend user model
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ('middle_name', 'prefix', 'job_title', 'address', 'office_phone', 'cell_phone', 'company')


class UserLogin(ModelForm):
    class Meta:
        fields = ['username', 'password']


class TestData(ModelForm):
    class Meta:
        model = models.Testresults
        fields = "__all__"


# Search Bar for searching Certificate Model
class SearchCertificates(ModelForm):
    class Meta:
        model = models.Certificate
        fields = ['report_number', 'product']
