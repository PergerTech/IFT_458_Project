from django.contrib import admin
from SolarPV.models import *


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Manufacturer, ManufacturerAdmin)


