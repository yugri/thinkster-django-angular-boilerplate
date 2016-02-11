from django.contrib import admin

from warehouse.models import Warehouse, Supply, StorageUnit, Supplier


class SupplyItemInline(admin.TabularInline):
    model = StorageUnit


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'warehouse', 'supplier', 'account', 'user', 'total',)
    inlines = [
        SupplyItemInline,
    ]


class StorageUnitAdmin(admin.ModelAdmin):
    list_display = ('arrival_date', 'product', 'warehouse', 'quantity', 'cost', 'total',)


admin.site.register(Warehouse)
admin.site.register(Supplier)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(StorageUnit, StorageUnitAdmin)

