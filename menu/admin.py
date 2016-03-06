from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from menu.models import ProductCategory, Product, ProductPrice
from warehouse.admin import SupplyItemInline


class ProductCategoryMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'department', 'sku', 'barcode', 'if_discountable')
    inlines = [
        ProductPriceInline,
        SupplyItemInline,
    ]


admin.site.register(ProductCategory, ProductCategoryMPTTModelAdmin)

admin.site.register(Product, ProductAdmin)
