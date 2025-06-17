from django.urls import path

from .views import DebtDelete
from .views import DebtEdit
from .views import Debts


app_name = 'debts'

urlpatterns = [
    path('', Debts.as_view(), name='debts'),
    path('<int:pk>/deletar/', DebtDelete.as_view(), name='delete'),
    path('<int:pk>/editar/', DebtEdit.as_view(), name='edit'),
]
