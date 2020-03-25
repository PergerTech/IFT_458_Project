from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import csv, io


def index(request):
    if request.method == 'post':
        user_form = UserRegistration(request.POST or None)
        if user_form.is_valid():
            return HttpResponseRedirect('/submit_success')
    else:
        user_form = UserRegistration()

    return render(request, 'index.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/user_portal')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "user_login.html", {"form": form})


def user_portal(request):
    return render(request, 'user_portal.html', {})


def registerUser(request):
    if request.method == 'post':
        user_form = UserRegistration(request.POST or None)
        if user_form.is_valid():
            return HttpResponseRedirect('/submit_success')
    else:
        user_form = UserRegistration()
    return render(request, 'user_registration.html', {'user_from': user_form})


def registerProduct(request):
    if request.method == 'POST':
        product_form = ProductRegistration(request.POST or None)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect('/submit_success')
    else:
        product_form = ProductRegistration()
    context = {'product_form': product_form}
    return render(request, 'productRegistration.html', context)


def registerManufacturer(request):
    if request.method == 'POST':
        manufacturer_form = ManufacturerRegistration(request.POST or None)
        if manufacturer_form.is_valid():
            manufacturer_form.save()
            return HttpResponseRedirect('/submit_success')
    else:
        manufacturer_form = ManufacturerRegistration()
    context = {'manufacturer_form': manufacturer_form}
    return render(request, 'manufacturer_registration.html', context)


def submit_success(request):
    return render(request, 'submit_success.html')


def upload_test(request):
    data = models.Testresults.objects.all()
    prompt = {
        'order':
            'Order of the CSV should be, Model Number, Test Sequence, Condition, Date, Isc, Voc, Imp, Vmp, FF, Pmp NOCT '
    }
    if request.method == "POST":
        return render(request, 'upload_testdata.html', prompt)

    # take in CSV file from request
    csv_file = request.FILES['file']

    # check if is CVS file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "File select is not a CSV file!")

    data_set = csv_file.r
    return render(request, 'upload_testdata.html', context)