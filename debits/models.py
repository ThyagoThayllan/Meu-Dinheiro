from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import IntegerField


class Debt(Model):
    """Debt status"""
    ACTIVE = 1
    INACTIVE = 2

    DEBT_STATUS = [
        (ACTIVE, 'Ativa'),
        (INACTIVE, 'Inativa'),
    ]

    """Debt categories"""
    CREDIT_CARD = 3
    FINANCING = 4
    LOAN = 5
    PERSONAL = 6
    SPECIAL_CHECK = 7
    OTHERS = 8

    DEBT_CATEGORIES = [
        (CREDIT_CARD, 'Cartão de Crédito'),
        (FINANCING, 'Financiamento'),
        (LOAN, 'Empréstimo'),
        (PERSONAL, 'Pessoal'),
        (SPECIAL_CHECK, 'Cheque Especial'),
        (OTHERS, 'Outros'),
    ]

    amount = DecimalField('Valor da Dívida', decimal_places=2, max_digits=7)

    category = IntegerField('Categoria', choices=DEBT_CATEGORIES)

    created_at = DateTimeField('Criado em', auto_now_add=True)

    description = CharField('Descrição', max_length=255)

    financier = CharField('Financiador', max_length=55)

    installments = IntegerField('Parcelas')

    installments_paid = IntegerField('Parcelas Pagas')

    is_paid = BooleanField('Paga?', default=False)

    status = IntegerField('Status da Dívida', choices=DEBT_STATUS)

    updated_at = DateTimeField('Editado em', auto_now=True)

    # TODO(@ThyagoThayllan):    Relate User to a Debt.
    """User related to a Debt.

        - User has multiple Debts.
    """
    # user = ForeignKey(User)

    def __str__(self) -> str:
        return f'{self.financier} | {self.amount} | {self.status_name}'

    @property
    def category_name(self):
        return self.get_category_display()

    @property
    def installment_amount(self):
        return self.amount / self.installments

    @property
    def remaining_amount(self):
        return self.amount - (self.installment_amount * self.installments_paid)

    @property
    def status_name(self):
        return self.get_status_display()
