from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_product', views.registerProduct, name="register product")
]