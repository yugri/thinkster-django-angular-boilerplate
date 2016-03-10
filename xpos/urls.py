# .. Imports
from rest_framework_nested import routers

from views import IndexView
from authentication.views import AccountViewSet, LoginView, LogoutView

from django.contrib import admin
from django.conf.urls import include, url


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    # ... URLs
    # Bound Django admin interface
    # url(r'^admin/', admin.site.urls),

    # Warehouse app URLs
    # url(r'^warehouse/', include('warehouse.urls')),

    # Menu app URLs
    # url(r'^menu/', include('menu.urls')),

    # Single page POS app Angular initialization url
    url(r'^pos/', include('sales.urls')),

    # API V1 URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    # url('^.*$', IndexView.as_view(), name='index'),
]
