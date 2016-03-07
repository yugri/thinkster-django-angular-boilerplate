from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from menu.models import ProductCategory, Product


class ProductsList(ListView):
    model = Product
    context_object_name = 'products'


class ProductCategoriesList(ListView):
    model = ProductCategory
    context_object_name = 'product_categories'


# def show_categories(request):
#     return render_to_response("menu/productcategory_list.html",
#                               {'nodes': ProductCategory.objects.all()},
#                               context_instance=RequestContext(request))
