from django.contrib import admin

from warehouse.models import Warehouse, Supply, SupplyItem, Supplier, WriteOff, WriteOffItem


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'warehouse', 'supplier', 'account', 'user', 'total',)
    inlines = [
        SupplyItemInline,
    ]


class WriteOffItemInline(admin.TabularInline):
    model = WriteOffItem


class WriteOffAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'warehouse', 'last_updated', 'user', 'total',)
    inlines = [
        WriteOffItemInline,
    ]

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]


admin.site.register(Warehouse)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(WriteOff, WriteOffAdmin)
admin.site.register(SupplyItem)
admin.site.register(Supplier)
