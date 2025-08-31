from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentication.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'cpf',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined',
    ]

    list_per_page = 100

    ordering = ['-last_login']

    search_fields = ['cpf', 'email', 'id', 'username']
