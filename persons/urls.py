from django.urls import path

from .views import Persons


urlpatterns = [
    path('', Persons.as_view(), name='persons'),
]
