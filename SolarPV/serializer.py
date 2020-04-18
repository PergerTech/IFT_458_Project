from rest_framework import serializers
from SolarPV import models


# Standard Model Serializer Endpoints
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certificate
        fields = '__all__'
        depth = 1


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Location
        fields = '__all__'
        depth = 1


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Standard
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


