from django.shortcuts import render

# Create your views here.
from api import models , serializers
from rest_framework import viewsets

#00
class HViewSet(viewsets.ModelViewSet):
    queryset = models.Hauntedhouse.objects.all()
    serializer_class = serializers.HSerializer

class RViewSet(viewsets.ModelViewSet):
    queryset = models.Renthouses.objects.all()
    serializer_class = serializers.RSerializer

#01
class FViewSet(viewsets.ModelViewSet):
    queryset = models.Firebrigade.objects.all()
    serializer_class = serializers.FSerializer

class PViewSet(viewsets.ModelViewSet):
    queryset = models.Policestation.objects.all()
    serializer_class = serializers.PSerializer

#02
class CViewSet(viewsets.ModelViewSet):
    queryset = models.Cvs.objects.all()
    serializer_class = serializers.CSerializer

class EViewSet(viewsets.ModelViewSet):
    queryset = models.Excellentmarket.objects.all()
    serializer_class = serializers.ESerializer

class HrtViewSet(viewsets.ModelViewSet):
    queryset = models.Hardwareretail.objects.all()
    serializer_class = serializers.HrtSerializer

class HstViewSet(viewsets.ModelViewSet):
    queryset = models.Hardwarestore.objects.all()
    serializer_class = serializers.HstSerializer

class RestViewSet(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestSerializer

#03
class WViewSet(viewsets.ModelViewSet):
    queryset = models.WChild.objects.all()
    serializer_class = serializers.WSerializer

