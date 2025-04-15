from django.forms import CharField
from django.forms import EmailField
from django.forms import EmailInput
from django.forms import Form
from django.forms import PasswordInput
from django.forms import TextInput


class LoginForm(Form):
    email = EmailField(
        label='E-mail',
        widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail...'})
    )

    password = CharField(
        label='Senha',
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha...'})
    )


class UserForm(Form):
    cpf = CharField(
        label='CPF',
        max_length=11,
        min_length=11,
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF...'}),
    )

    email = EmailField(
        label='E-mail',
        widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail...'})
    )

    first_name = CharField(
        label='Nome',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'})
    )

    last_name = CharField(
        label='Sobrenome',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome...'})
    )

    password = CharField(
        label='Senha',
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha...'})
    )

    username = CharField(
        label='Usuário',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário...'})
    )
