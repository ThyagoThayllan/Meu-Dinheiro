from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField


class User(AbstractUser):
    REQUIRED_FIELDS = ['cpf', 'password', 'username']
    USERNAME_FIELD = 'email'

    cpf = CharField(
        'CPF',
        max_length=11,
        unique=True,
        error_messages={'unique': 'A user with that CPF already exists.'},
    )

    email = EmailField(
        'E-mail',
        unique=True,
        error_messages={'unique': 'A user with that E-mail already exists.'},
    )

    first_name = CharField('Nome', max_length=55)

    last_name = CharField('Sobrenome', max_length=55)

    password = CharField('Senha', max_length=128)

    username = CharField('Usuário', max_length=55)

    def __str__(self) -> str:
        return f'{self.pk} - {self.email} - {self.full_name}'

    @property
    def full_name(self) -> str:
        return super().get_full_name()
