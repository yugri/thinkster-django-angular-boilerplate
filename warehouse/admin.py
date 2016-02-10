from django.contrib import admin

from warehouse.models import Warehouse, Supply, SupplyItem, Supplier


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'account', 'user', 'total',)
    inlines = [
        SupplyItemInline,
    ]


admin.site.register(Warehouse)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(SupplyItem)
admin.site.register(Supplier)
