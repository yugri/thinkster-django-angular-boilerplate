from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=55, blank=False)
    currency = models.CharField(max_length=3, blank=False)
    type = models.CharField(max_length=1, blank=False)
    balance = models.DecimalField(decimal_places=2, default=0.00)