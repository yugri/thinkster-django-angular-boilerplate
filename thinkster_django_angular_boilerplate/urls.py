# .. Imports
from rest_framework_nested import routers

from views import IndexView
from authentication.views import AccountViewSet

from django.conf.urls import include, patterns, url

router = routers.SimpleRouter()
router.register(r'account', AccountViewSet)

urlpatterns = patterns(
    '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)
