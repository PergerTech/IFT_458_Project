if __name__ == '__main__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IFT458_Project.settings")
    django.setup()

    from SolarPV import models

    test_data = models.Testresults.objects.all().filter(product=1)
    for item in test_data:
        print(item.isc)