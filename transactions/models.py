from django.conf import settings

from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import DecimalField


class Transaction(Model):
    """Transaction types"""
    EXPENSE = 1
    INCOME = 2

    TRANSACTION_TYPES = [
        (EXPENSE, 'Saída'),
        (INCOME, 'Entrada'),
    ]

    """Transaction categories"""
    CLOTHING = 1
    DEBIT = 2
    EDUCATION = 3
    FOOD = 4
    GIFT = 5
    HEALTH = 6
    HOUSING = 7
    INVESTMENT = 8
    LEISURE = 9
    PET = 10
    TECHNOLOGY = 11
    TRANSPORT = 12
    OTHERS = 13

    CATEGORIES = [
        (CLOTHING, 'Vestuário'),
        (DEBIT, 'Dívidas'),
        (EDUCATION, 'Educação'),
        (FOOD, 'Alimentação'),
        (GIFT, 'Presentes'),
        (HEALTH, 'Saúde'),
        (HOUSING, 'Moradia'),
        (INVESTMENT, 'Investimentos'),
        (LEISURE, 'Lazer'),
        (PET, 'Pets'),
        (TECHNOLOGY, 'Tecnologia'),
        (TRANSPORT, 'Transporte'),
        (OTHERS, 'Outros'),
    ]

    amount = DecimalField('Valor', decimal_places=2, max_digits=10)

    category = IntegerField('Categoria', choices=CATEGORIES)

    created_at = DateTimeField('Criado em', auto_now_add=True)

    date = DateField('Data', blank=True, null=True)

    description = CharField('Descrição', blank=True, max_length=255)

    destination = CharField('Destino', max_length=55)

    # TODO(@ThyagoThayllan):    Transaction file field.
    #   document = FileField()

    is_paid = BooleanField('Pago?', default=True)

    # TODO(@ThyagoThayllan):    Relate Person to a Transaction.
    """Person related to a Transaction.

        - A Person can be related to many Transactions.
        - A Transaction may or may not have a related Person.
    """
    # person = ForeignKey(Person, blank=True, null=True)

    transaction_type = IntegerField('Tipo', choices=TRANSACTION_TYPES)

    updated_at = DateTimeField('Editado em', auto_now=True)

    """User related to a Transaction.

        - User has multiple Transactions.
    """
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='transactions',
        related_query_name='transaction',
    )

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'

    def __str__(self) -> str:
        return f'{self.id} - {self.destination} - {self.amount} - {self.transaction_type_name}'

    @property
    def category_name(self):
        return self.get_category_display()

    @property
    def transaction_type_name(self):
        return self.get_transaction_type_display()
