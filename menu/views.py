from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Product


class ProductsList(ListView):
    model = Product
    context_object_name = 'products'
