from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from finances.models import FinCategory, FinAccount, CashShift, Transaction


class FinCategoryMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    # mptt_indent_field = "name"
    list_display = ("tree_actions", "indented_title", "parent", "apply_revenues", "apply_wastes")


class FinAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "currency", "type", "balance")


class CashShiftAdmin(admin.ModelAdmin):
    list_display = ("__str__" or "__unicode__", "datetime_opened", "datetime_closed", "is_closed", "cash_total",
                    "encashment")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("__str__" or "__unicode__", "trans_type", "category", "date_created", "amount", "comment")

admin.site.register(FinCategory, FinCategoryMPTTModelAdmin)
admin.site.register(FinAccount, FinAccountAdmin)
admin.site.register(CashShift, CashShiftAdmin)
admin.site.register(Transaction, TransactionAdmin)


