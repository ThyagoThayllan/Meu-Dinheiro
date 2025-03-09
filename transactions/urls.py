from django.urls import path

from .views import Transactions


urlpatterns = [
    path('', Transactions.as_view(), name='transactions')
]
