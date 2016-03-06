from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from headquarter.models import SellPoint


class ProductManager(models.Manager):
    pass


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    MEASURE_UNIT_CHOICES = (
        ('pcs.', _('pieces')),  # '....'
        ('l', _('liter')),      # '0138'
        ('kg', _('kilogram')),  # '0301'
        ('box', _('box')),      # '2075'
        ('set', _('set')),      # '2398'
    )
    PRODUCT_TYPE_CHOICES = (
        ('good', _('Good')),
        ('ingredient', _('Ingredient')),
        ('service', _('Service')),
    )
    name = models.CharField(max_length=128, blank=False, help_text=_('Specify product/ingredient name'))
    type = models.CharField(max_length=50, blank=False, choices=PRODUCT_TYPE_CHOICES, null=True)
    measure_units = models.CharField(max_length=5, choices=MEASURE_UNIT_CHOICES, blank=True,
                                     null=True, help_text=_('Choose the measure units'))
    category = models.ManyToManyField(ProductCategory, blank=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=15, blank=True, null=True)
    if_discountable = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def prices(self):
        prices = ProductPrice.objects.filter(product=self)
        return prices


class ProductPrice(models.Model):
    product = models.ForeignKey(Product)
    sell_point = models.ForeignKey(SellPoint)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True)
    # cost = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, blank=True, null=True)
    markup = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)