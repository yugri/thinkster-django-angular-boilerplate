from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from menu.models import Ingredient


class Warehouse(models.Model):
    date_created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=55, blank=False, help_text=_('Specify the warehouse name'))
    address = models.TextField(max_length=255, help_text=_('Add address'))
    # shop = models.ForeignKey()

    def __str__(self):
        return self.name


class Supply(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey('Supplier', help_text=_('Choose the supplier or add one'))
    account = models.ForeignKey('Account', help_text=_('Set a debit account'))

    products = models.ManyToManyField('Ingredient', help_text=_('Choose one from products list'))

    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = _("supplies")

    def __str__(self):              # __unicode__ on Python 2
        return "-".join(["#%d" % self.pk, _("%s") % self.date_created])


class Supplier(models.Model):
    name = models.CharField(max_length=128, blank=False, help_text='Define the supplier\'s name')

    def __str__(self):
        return self.name