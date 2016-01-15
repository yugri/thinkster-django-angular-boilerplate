from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True


class SellPoint(models.Model):
    name = models.CharField(max_length=128, blank=False, null=True, unique=True)
