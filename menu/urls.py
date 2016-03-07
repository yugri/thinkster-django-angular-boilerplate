from django.conf.urls import url

from menu.views import ProductCategoriesList, ProductsList

urlpatterns = [
    # Warehouse Index View URL
    url(r'^products', ProductsList.as_view(), name='products'),
    # url(r'^product-categories', show_categories, name='product-categories'),
    url(r'^product-categories', ProductCategoriesList.as_view(), name='product-categories'),
]