from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('transacoes/', include('transactions.urls')),
    path('dividas/', include('debts.urls')),
    path('pessoas/', include('persons.urls')),
]
