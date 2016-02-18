from django.contrib import admin

from warehouse.models import Warehouse, Supply, StorageUnit, Supplier, WriteOff, WriteOffUnit


class SupplyItemInline(admin.TabularInline):
    model = StorageUnit


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'warehouse', 'supplier', 'account', 'user', 'total',)
    inlines = [
        SupplyItemInline,
    ]


class StorageUnitAdmin(admin.ModelAdmin):
    list_display = ('arrival_date', 'product', 'warehouse', 'quantity', 'cost', 'total',)


class WriteOffItemInline(admin.TabularInline):
    model = WriteOffUnit


class WriteOffAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'warehouse', 'last_updated', 'user')
    inlines = [
        WriteOffItemInline,
    ]


class WriteOffUnitAdmin(admin.ModelAdmin):
    list_display = ('init_date', 'product', 'warehouse', 'quantity',)

admin.site.register(Warehouse)
admin.site.register(Supplier)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(StorageUnit, StorageUnitAdmin)
admin.site.register(WriteOff, WriteOffAdmin)
admin.site.register(WriteOffUnit, WriteOffUnitAdmin)

