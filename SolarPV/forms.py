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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('address', 'office_phone', 'cell_phone')



class UserLogin(ModelForm):
    class Meta:
        fields = ['username', 'password']


class TestData(ModelForm):
    class Meta:
        model = models.Testresults
        fields = "__all__"

