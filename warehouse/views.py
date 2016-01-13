from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from warehouse.models import Supply


class SuppliesList(ListView):
    model = Supply
    context_object_name = 'last_supplies'
