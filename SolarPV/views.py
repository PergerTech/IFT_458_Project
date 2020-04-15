from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import csv, io
from datetime import datetime
from SolarPV import models
from rest_framework import viewsets
from .serializer import CertificateSerializer, LocationSerializer, StandardSerializer, ServiceSerializer, ClientSerializer

from SolarPV.models import Testresults, Product


def index(request):
    context = {}
    return render(request, 'index.html', context)


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


@login_required
def user_portal(request):
    products = Product.objects.filter(manufacturer__contact_person__username= request.user.username)
    context = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'cell': request.user.profile.cell_phone,
        'office': request.user.profile.office_phone,
        'address': request.user.profile.address,
        'products': products
    }
    return render(request, 'user_portal.html', context)


@transaction.atomic
def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            return redirect('user created')
        else:
            return HttpResponse("Username already used")
    else:
        logout(request)
        form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, 'user_registration.html', {'form': form, 'profile_form': profile_form})


def userCreated(request):
    return render(request, 'user_created.html', {})


@login_required
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


@login_required
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


def product(request, product_id):

    product_data = models.Product.objects.select_related('manufacturer').get(pk=product_id)
    test_data = models.Testresults.objects.all().filter(product=product_id)
    # test_data_tc200 = test_data.get(test_sequence__contains="TC200")
    # test_data_dampheat = test_data.get(test_sequence__contains="Damp Heat")
    # test_data_hf10 = test_data.get(test_sequence__contains="HF10")

    context = {
        "product_model": product_data.model_number,
        "manufacturer": product_data.manufacturer.company_name,
        "contact_person": product_data.manufacturer.contact_person.first_name + " " + product_data.manufacturer.contact_person.last_name,
        "contact_email": product_data.manufacturer.contact_person.email,
        "cell_technology": product_data.cell_technology,
        "test_data": test_data
    }
    return render(request, 'product_view.html', context)


@login_required
def upload_csv(request):
    template = 'upload_csv.html'

    prompt = {
        'order': 'CVS column order: Model, Test, Sequence, Condition, Test Date, Isc, Voc, Imp, Vmp, FF, Pmp, Noct'
    }
    # Return input view to user
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['csv_file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a csv file")
        return HttpResponseRedirect('upload test')
    else:
        dataset = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(dataset)
        next(io_string)
        for column in csv.reader(io_string, delimiter=",", quotechar="|"):
            date_object = datetime.strptime(column[3], '%m/%d/%Y').strftime('%Y-%m-%d')

            product_id = Product.objects.get(model_number=column[0])

            noct_column = column[10]
            try:
                float(noct_column)
            except:
                noct_column = None

            _, created = Testresults.objects.update_or_create(
                product=product_id,
                test_sequence=column[1],
                report_condition=column[2],
                test_date=date_object,
                isc=column[4],
                voc=column[5],
                imp=column[6],
                vmp=column[7],
                ff=column[8],
                pmp=column[9],
                noct=noct_column
            )
        context = {}
        return render(request, 'submit_success.html', context)


# SolarPV API serializers

class CertificateView(viewsets.ModelViewSet):
    queryset = models.Certificate.objects.all()
    serializer_class = CertificateSerializer


class LocationView(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = LocationSerializer


class StandardView(viewsets.ModelViewSet):
    queryset = models.Standard.objects.all()
    serializer_class = StandardSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = ServiceSerializer


