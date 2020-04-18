from django.urls import path, include
from . import views
from rest_framework import routers

# SolarPV API endpoint registration
router = routers.DefaultRouter()
router.register('Certificates', views.CertificateView)
router.register('Locations', views.LocationView)
router.register('Services', views.ServiceView)
router.register('Clients', views.ClientView)
router.register('Standards', views.StandardView)

# URL directory for SolarPV
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register_product', views.registerProduct, name="register product"),
    path('submit_success', views.submit_success, name="submit success"),
    path('manufacturer_registration', views.registerManufacturer, name='register manufacturer'),
    path('register_user', views.registerUser, name="register user"),
    path('user_login', views.user_login, name='user login'),
    path('user_portal', views.user_portal, name='user portal'),
    path('upload_test', views.upload_csv, name='upload test'),
    path('user_created', views.userCreated, name='user created'),
    path('product/<int:product_id>', views.product, name='product view'),
    path('certificates', views.certificates, name='certificates'),
    path('api_index/', include(router.urls)),
    ]
