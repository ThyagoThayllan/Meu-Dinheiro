from django.urls import path

from .views import Transactions


app_name = 'transactions'

urlpatterns = [
    path('', Transactions.as_view(), name='transactions')
]
