from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class IngredientManager(models.Manager):
    pass


class Ingredient(models.Model):
    MEASURE_UNIT_CHOICES = (
        ('pcs.', _('pieces')),  # '....'
        ('l', _('liter')),      # '0138'
        ('kg', _('kilogram')),  # '0301'
        ('box', _('box')),      # '2075'
        ('set', _('set')),      # '2398'
    )
    name = models.CharField(max_length=128, blank=False, help_text=_('Specify ingredient/product name'))
    sku = models.CharField(max_length=50, help_text=_('Stock Keeping Unit'))
    measure_units = models.CharField(max_length=5, choices=MEASURE_UNIT_CHOICES, blank=False,
                                     help_text=_('Choose the measure units'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name