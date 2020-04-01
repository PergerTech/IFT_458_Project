from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import csv, io
from datetime import datetime

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
    return render(request, 'user_portal.html', {})


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user created')
    else:
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


@login_required
def upload_csv(request):
    template = 'upload_csv.html'

    prompt = {
        'order': "Oder of CSV should be ..."
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






