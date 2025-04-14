from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db.models import CharField
from django.db.models import EmailField


class User(AbstractUser):
    REQUIRED_FIELDS = ['cpf', 'password', 'username']
    USERNAME_FIELD = 'email'

    cpf = CharField(
        'CPF',
        validators=[MinLengthValidator(11, message='O CPF precisa ter 11 caracteres.')],
        max_length=11,
        unique=True,
        error_messages={'unique': 'Já existe um usuário com esse CPF.'},
    )

    email = EmailField(
        'E-mail',
        unique=True,
        error_messages={'unique': 'Já existe um usuário com esse e-mail.'},
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
