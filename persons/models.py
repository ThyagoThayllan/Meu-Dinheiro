from django.db.models import Model
from django.db.models import CharField
from django.db.models import EmailField


class Person(Model):
    """Debit related to a Person"""
    # debit = ForeignKey()

    email = EmailField('E-mail')

    name = CharField('Nome', max_length=55)

    phone = CharField('Telefone', max_length=11)

    """Transaction related to a Person"""
    # transaction = ForeignKey()
