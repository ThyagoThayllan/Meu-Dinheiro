from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import ForeignKey
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

    MAXIMUM_FINANCING_TERM = 420
    MINIMUM_FINANCING_TERM = 1

    amount = DecimalField(
        'Valor da Dívida',
        decimal_places=2,
        max_digits=10,
        validators=[
            MaxValueValidator(99999999.99),
            MinValueValidator(0.01),
        ],
    )

    category = IntegerField('Categoria', choices=DEBT_CATEGORIES)

    created_at = DateTimeField('Criado em', auto_now_add=True)

    description = CharField('Descrição', max_length=100)

    financier = CharField('Financiador', blank=True, max_length=55, null=True)

    installments = IntegerField(
        'Parcelas',
        validators=[
            MinValueValidator(MINIMUM_FINANCING_TERM),
            MaxValueValidator(MAXIMUM_FINANCING_TERM),
        ],
    )

    installments_paid = IntegerField('Parcelas Pagas')

    is_paid = BooleanField('Paga?', default=False)

    updated_at = DateTimeField('Editado em', auto_now=True)

    """User related to a Debt.

        - User has multiple Debts.
    """
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='debts',
        related_query_name='debt',
    )

    class Meta:
        verbose_name = 'Dívida'
        verbose_name_plural = 'Dívidas'

    def __str__(self) -> str:
        return f'{self.id} - {self.description} - {self.amount} - {self.status}'

    @property
    def category_name(self):
        return self.get_category_display()

    @property
    def installment_amount(self):
        return round(self.amount / self.installments, 2)

    @property
    def remaining_amount(self):
        return self.amount - (self.installment_amount * self.installments_paid)

    @property
    def status(self):
        return 'Inativa' if self.is_paid else 'Ativa'

    def clean(self):
        super().clean()

        if self.installments_paid > self.installments:
            raise ValidationError(
                {
                    'installments_paid': (
                        'Quantidade de parcelas pagas não pode ser maior do que o total de '
                        'parcelas.'
                    )
                }
            )
