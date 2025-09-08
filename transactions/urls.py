from django.urls import include
from django.urls import path

from .views import TransactionDelete
from .views import TransactionEdit
from .views import Transactions


app_name = 'transactions'

urlpatterns = [
    path('', Transactions.as_view(), name='transactions'),
    path('<int:pk>/deletar/', TransactionDelete.as_view(), name='delete'),
    path('<int:pk>/editar/', TransactionEdit.as_view(), name='edit'),
    path('ajax/', include('transactions.ajax_urls')),
]
