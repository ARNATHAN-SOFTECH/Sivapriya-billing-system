from django.contrib import admin
from .models import (
    Treatment,
    Medicine,
    Bill,
    BillItem,
)


# ============================================================
# TREATMENT ADMIN
# ============================================================

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "amount",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )


# ============================================================
# MEDICINE ADMIN
# ============================================================

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "amount",
        "stock",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )


# ============================================================
# BILL ITEM INLINE
# ============================================================

class BillItemInline(admin.TabularInline):

    model = BillItem

    extra = 0

    fields = (
        "item_type",
        "item_name",
        "quantity",
        "unit_price",
        "total_amount",
        "treatment",
        "medicine",
    )

    readonly_fields = (
        "total_amount",
    )


# ============================================================
# BILL ADMIN
# ============================================================

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "bill_number",
        "patient",
        "grand_total",
        "paid_amount",
        "balance_amount",
        "status",
        "payment_method",
        "bill_date",
    )

    list_filter = (
        "status",
        "payment_method",
        "bill_date",
    )

    search_fields = (
        "bill_number",
        "patient__name",
        "patient__op_number",
        "payment_reference",
    )

    readonly_fields = (
        "bill_number",
        "bill_date",
    )

# ============================================================
# BILL ITEM ADMIN
# ============================================================

@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):

    list_display = (
        "bill",
        "item_type",
        "item_name",
        "quantity",
        "unit_price",
        "total_amount",
    )

    search_fields = (
        "item_name",
        "bill__bill_number",
    )

    list_filter = (
        "item_type",
    )

    ordering = (
        "-id",
    )