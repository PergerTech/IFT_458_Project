from django.contrib import admin
from SolarPV.models import *


# User Extension view
class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


# Manufacturer admin view
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person', 'registered_country')
    fields = ('company_name', 'contact_person', 'registered_country')
    list_filter = ('company_name', 'manufacturer_id', 'registered_country')


admin.site.register(Manufacturer, ManufacturerAdmin)


# Product admin view
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


# Client admin view
class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)


# Location admin view
class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)


# Standard admin view
class StandardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Standard, StandardAdmin)


# Certificate admin view
class CertificateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Certificate, CertificateAdmin)



admin.site.site_header = "SolarPV Admin Portal"
admin.site.site_title = "SolarPV Admin"
admin.site.index_title = "Welcome to SolarPV Staff Portal"
