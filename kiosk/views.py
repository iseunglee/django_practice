from django.shortcuts import render
from django.views.generic import ListView, DetailView
from kiosk.models import DrinkType, Menu
# Create your views here.

class DrinkTypeLV(ListView):
    model = DrinkType