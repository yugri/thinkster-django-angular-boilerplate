from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class SellPoint(models.Model):
    name = models.CharField(max_length=128, blank=False, help_text=_('Sell point name'))
    address = models.CharField(max_length=50, blank=False, null=True)
    terminal_login = models.CharField(max_length=50, blank=True, null=True)
    warehouses = models.ManyToManyField('warehouse.Warehouse', blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name