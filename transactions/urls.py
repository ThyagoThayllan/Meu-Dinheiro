from django.urls import include
from django.urls import path

from .views import DeleteTransaction
from .views import EditTransaction
from .views import Transactions


app_name = 'transactions'

urlpatterns = [
    path('', Transactions.as_view(), name='transactions'),
    path('<int:pk>/editar/', EditTransaction.as_view(), name='edit'),
    path('<int:pk>/deletar/', DeleteTransaction.as_view(), name='delete'),
    path('ajax/', include('transactions.ajax_urls')),
]
