from django.contrib import admin
from django.contrib.admin import ModelAdmin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = [
        'id',
        'destination',
        'amount',
        'category',
        'transaction_type',
        'date',
        'is_paid',
        'created_at',
        'updated_at',
    ]

    list_filter = ['is_paid', 'category', 'transaction_type', 'date', 'created_at', 'updated_at']

    list_per_page = 100

    ordering = ['-created_at']

    search_fields = [
        'amount',
        'destination',
        'id',
    ]
