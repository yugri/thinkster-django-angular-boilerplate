# .. Imports
from rest_framework_nested import routers

from views import IndexView
from authentication.views import AccountViewSet, LoginView, LogoutView

from django.contrib import admin
from django.conf.urls import include, patterns, url


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    # ... URLs
    # Warehouse app URLs
    url(r'^warehouse/', include('warehouse.urls')),

    # Bound Django admin interface
    url(r'^admin/', admin.site.urls),

    # API V1 URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url('^.*$', IndexView.as_view(), name='index'),
]
