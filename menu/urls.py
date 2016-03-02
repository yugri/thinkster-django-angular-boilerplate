from django.conf.urls import url

from menu.views import ProductsList

urlpatterns = [
    # Warehouse Index View URL
    url(r'^products', ProductsList.as_view(), name='products'),
]