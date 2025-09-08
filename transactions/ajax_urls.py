from django.urls import path

from transactions.ajax_views import TransactionsAjax


urlpatterns = [
    path('<str:period>/', TransactionsAjax.as_view(), name='ajax-list'),
]
