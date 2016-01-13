from django.contrib import admin

from warehouse.models import Warehouse, Supply, Supplier

admin.site.register(Warehouse)
admin.site.register(Supply)
admin.site.register(Supplier)
