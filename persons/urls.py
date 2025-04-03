from django.urls import path

from .views import Persons


app_name = 'persons'

urlpatterns = [
    path('', Persons.as_view(), name='persons'),
]
