from django.contrib import admin
from SolarPV.models import *


# User Extension view
class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


# Manufacturer admin view
class ManufacturerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Manufacturer, ManufacturerAdmin)


# Product admin view
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)

