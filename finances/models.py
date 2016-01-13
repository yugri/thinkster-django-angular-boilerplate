from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class FinAccount(models.Model):
    FIN_ACCOUNT_TYPE_CHOICES = (
        (1, _('Cash')),
        (2, _('Cashless')),
        (3, _('Bank Card'))
    )

    CURRENCY_CHOICES = (
        (980, 'UAH'),
        (810, 'RUR'),
        (974, 'BYR'),
        (840, 'USD')
    )
    name = models.CharField(max_length=55, blank=False)
    currency = models.PositiveSmallIntegerField(blank=False, choices=CURRENCY_CHOICES)
    type = models.PositiveIntegerField(blank=False, choices=FIN_ACCOUNT_TYPE_CHOICES)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name