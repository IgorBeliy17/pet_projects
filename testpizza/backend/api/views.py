from django.shortcuts import render
from rest_framework import viewsets
from pizza.models import Pizza
from api.serializers import PizzaSerializer


# Create your views here.
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

