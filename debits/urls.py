from django.urls import path

from .views import Debts

urlpatterns = [
    path('', Debts.as_view(), name='debts')
]
