from __future__ import unicode_literals

import decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from authentication.models import Account
from menu.models import Ingredient
from finances.models import FinAccount


class Warehouse(models.Model):
    date_created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=55, blank=False, help_text=_('Specify the warehouse name'))
    address = models.TextField(max_length=255, help_text=_('Add address'))
    # shop = models.ForeignKey()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Supply(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey('Supplier', help_text=_('Choose the supplier or add one'))
    account = models.ForeignKey(FinAccount, help_text=_('Set a debit account'))
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Account, null=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = _("supplies")

    def __str__(self):              # __unicode__ on Python 2
        return "-".join(["#%d" % self.pk, _("%s") % self.date_created])

    def __unicode__(self):
        return "-".join(["#%d" % self.pk, _("%s") % self.date_created])

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        supply_items = SupplyItem.objects.filter(supply=self)
        for item in supply_items:
            total += item.total
        return total


class SupplyItem(models.Model):
    product = models.ForeignKey(Ingredient, help_text=_('Select product/ingredient'))
    quantity = models.DecimalField(max_digits=9, decimal_places=3, default=0.000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    supply = models.ForeignKey(Supply, blank=True, null=True, help_text=_('Add related supply'))

    def __str__(self):
        return '%s (%s)' % (self.product.name, self.product.sku)

    def __unicode__(self):
        return '%s (%s)' % (self.product.name, self.product.sku)

    @property
    def total(self):
        return self.quantity * self.price

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku


class Supplier(models.Model):
    name = models.CharField(max_length=128, blank=False, help_text='Define the supplier\'s name')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

