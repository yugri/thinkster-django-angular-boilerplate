from django.contrib import admin
from warehouse.models import Warehouse, Supply, SupplyItem, Supplier


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem
    extra = 0


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('__str__' or '__unicode__', 'date_created', 'supplier', 'user')
    inlines = [SupplyItemInline,]


admin.site.register(Warehouse)
admin.site.register(Supply, SupplyAdmin)
# admin.site.register(Supply)
# admin.site.register(SupplyItem)
admin.site.register(Supplier)
