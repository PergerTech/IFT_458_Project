from django import forms


class ProductRegistration(forms.Form):
    manufacturer = forms.CharField(label="Manufacturer", max_length=100)
#     location = forms.CharField(label="Location", max_length=100),
#     contact = forms.CharField(label="Contact", max_length=100),
#     address = forms.CharField(label="Address", max_length=100),
#     email = forms.EmailField(label='Email'),
#     phone = forms