from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_product', views.registerProduct, name="register product"),
    path('submit_success', views.submit_success, name="submit_success"),
    path('manufacturer_registration', views.registerManufacturer, name='register manufacturer')
]