from django.contrib import admin
from django.contrib.admin import ModelAdmin

from debts.models import Debt


@admin.register(Debt)
class DebtAdmin(ModelAdmin):
    list_display = [
        'id',
        'description',
        'category',
        'amount',
        'is_paid',
        'updated_at',
        'created_at',
    ]

    list_filter = ['category', 'updated_at', 'created_at', 'is_paid']

    list_per_page = 100

    ordering = ['-created_at']

    search_fields = [
        'amount',
        'category',
        'description',
        'financier',
        'id',
    ]
