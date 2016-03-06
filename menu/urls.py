from django.conf.urls import url

from menu.views import ProductCategoriesList, ProductsList, show_categories

urlpatterns = [
    # Warehouse Index View URL
    url(r'^products', ProductsList.as_view(), name='products'),
    url(r'^product-categories', show_categories, name='product-categories'),
]