from django.urls import path

from .views import DeleteTransaction
from .views import NewTransaction
from .views import Transactions


app_name = 'transactions'

urlpatterns = [
    path('', Transactions.as_view(), name='transactions'),
    path('cadastrar/', NewTransaction.as_view(), name='register'),
    path('<int:pk>/deletar/', DeleteTransaction.as_view(), name='delete'),
]
