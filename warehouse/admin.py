from django.contrib import admin

from warehouse.models import Warehouse, Supply, SupplyItem, Supplier

admin.site.register(Warehouse)
admin.site.register(Supply)
admin.site.register(SupplyItem)
admin.site.register(Supplier)
