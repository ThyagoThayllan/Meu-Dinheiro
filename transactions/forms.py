from django.forms import CheckboxInput
from django.forms import ModelForm
from django.forms import NumberInput
from django.forms import Select
from django.forms import TextInput

from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'category',
            'date',
            'description',
            'destination',
            'is_paid',
            'transaction_type',
        ]
        widgets = {
            'amount': NumberInput(
                attrs={'class': 'form-control mb-2', 'placeholder': 'Valor da transação...'}
            ),
            'category': Select(attrs={'class': 'form-select mb-2'}),
            'date': TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'DD/MM/YYYY'}),
            'description': TextInput(
                attrs={'class': 'form-control mb-2', 'placeholder': 'Descrição da transação...'}
            ),
            'destination': TextInput(
                attrs={'class': 'form-control mb-2', 'placeholder': 'Destino da transação...'}
            ),
            'is_paid': CheckboxInput(attrs={'class': 'form-check-input mb-2 ms-2'}),
            'transaction_type': Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = [('', 'Selecionar...')] + sorted(
            Transaction.CATEGORIES, key=lambda key: key[1]
        )

        self.fields['transaction_type'].choices = [('', 'Selecionar...')] + sorted(
            Transaction.TRANSACTION_TYPES, key=lambda key: key[1]
        )
