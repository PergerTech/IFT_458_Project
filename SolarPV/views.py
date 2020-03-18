from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProductRegistration, ManufacturerRegistration
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def registerProduct(request):
    if request.method == 'POST':
        product_form = ProductRegistration(request.POST)
        if product_form.is_valid():
            return HttpResponseRedirect('/submit_success/')
    else:
        product_form = ProductRegistration()
    context = {'product_form': product_form}
    return render(request, 'productRegistration.html', context)


def registerManufacturer(request):
    if request == 'POST':
        manufacturer_form = ManufacturerRegistration(request.POST)
        if manufacturer_form.is_valid():
            return HttpResponseRedirect('/submit_success/')
    else:
        manufacturer_form = ManufacturerRegistration()
    context = {'manufacturer_form': manufacturer_form}
    return request(request, 'manufacturer_registration.html', context)


def submit_success(request):
    return render(request, 'submit_success.html')