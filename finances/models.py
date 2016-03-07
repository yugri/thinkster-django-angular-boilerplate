from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from headquarter.models import SellPoint


class FinCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    apply_revenues = models.BooleanField(default=True)
    apply_wastes = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'fin_category'
        verbose_name_plural = 'fin_categories'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


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


class CashShift(models.Model):
    sell_point = models.ForeignKey(SellPoint)
    datetime_opened = models.DateTimeField(auto_now_add=True)
    datetime_closed = models.DateTimeField(_("Specify date and time for closing cash shift"), blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    cash_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    encashment = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cash shift #%s opened %s" % (self.pk, self.datetime_opened)

    def __unicode__(self):
        return "Cash shift #%s opened %s" % (self.pk, self.datetime_opened)


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("revenue", _("Revenue")),
        ("waste", _("Waste")),
        ("transfer", _("Transfer"))
    )
    trans_type = models.CharField(choices=TRANSACTION_TYPES, max_length=24)
    fin_account = models.ForeignKey(FinAccount)
    category = models.ForeignKey(FinCategory)
    date_created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    comment = models.CharField(max_length=1024)

    def __str__(self):
        return "Transaction #%s created at %s" % (self.pk, self.date_created)

    def __unicode__(self):
        return "Transaction #%s created at %s" % (self.pk, self.date_created)