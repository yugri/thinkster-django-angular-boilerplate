# .. Imports
from rest_framework_nested import routers

from views import IndexView
from authentication.views import AccountViewSet, LoginView

from django.conf.urls import include, patterns, url

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),

    url('^.*$', IndexView.as_view(), name='index'),
)
