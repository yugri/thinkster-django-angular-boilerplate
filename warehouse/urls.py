from django.conf.urls import include, url
from warehouse.views import SuppliesList, WriteOffsList

urlpatterns = [
    # Warehouse Index View URL
    url(r'^supplies', SuppliesList.as_view(), name='supplies'),
    url(r'^write-offs', WriteOffsList.as_view(), name='write-offs'),
]