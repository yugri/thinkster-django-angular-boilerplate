from django.conf.urls import include, url
from warehouse.views import SuppliesList

urlpatterns = [
    # Warehouse Index View URL
    url(r'', SuppliesList.as_view()),
]