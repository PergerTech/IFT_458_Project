from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductRegistration
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def registerProduct(request):
    product_form = ProductRegistration(request.POST or None)
    context = {"product_form": product_form}
    return render(request, 'productRegistration.html', context)


