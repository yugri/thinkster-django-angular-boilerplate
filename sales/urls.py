from django.conf.urls import url
from sales.views import PosAppView

urlpatterns = [
    # Warehouse Index View URL
    url(r'', PosAppView.as_view(), name='pos'),
]