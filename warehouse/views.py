from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from warehouse.models import Supply, WriteOff


class SuppliesList(ListView):
    model = Supply
    context_object_name = 'supplies'


class WriteOffsList(ListView):
    model = WriteOff
    context_object_name = 'write_offs'
