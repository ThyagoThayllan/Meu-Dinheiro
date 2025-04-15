from django.urls import path

from .views import Login
from .views import Logout
from .views import SignUp

app_name = 'authentication'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
]
