from django.urls import path

from .views import Debits

urlpatterns = [
    path('', Debits.as_view(), name='debits')
]
