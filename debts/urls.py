from django.urls import path

from .views import Debts


app_name = 'debts'

urlpatterns = [
    path('', Debts.as_view(), name='debts')
]
