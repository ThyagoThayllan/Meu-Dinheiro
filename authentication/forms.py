from django.forms import EmailInput
from django.forms import ModelForm
from django.forms import PasswordInput
from django.forms import TextInput

from .models import User


class LoginForm(ModelForm):
    class Meta:
        model = User

        fields = ['email', 'password']

        widgets = {
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail...'}
            ),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite sua senha...'}
            ),
        }


class SignUpForm(ModelForm):
    class Meta:
        model = User

        fields = ['cpf', 'email', 'first_name', 'last_name', 'password', 'username']

        widgets = {
            'cpf': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF...'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail...'}
            ),
            'first_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'}
            ),
            'last_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome...'}
            ),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite sua senha...'}
            ),
            'username': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário...'}
            ),
        }
