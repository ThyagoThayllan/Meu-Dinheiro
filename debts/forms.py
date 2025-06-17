from django.forms import CheckboxInput
from django.forms import NumberInput
from django.forms import Select
from django.forms import TextInput
from django.forms import ModelForm

from .models import Debt


class DebtForm(ModelForm):
    class Meta:
        model = Debt

        fields = [
            'amount',
            'category',
            'description',
            'financier',
            'installments',
            'installments_paid',
        ]

        widgets = {
            'amount': NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite o valor...'}
            ),
            'category': Select(attrs={'class': 'form-select'}),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite uma descrição. Ex: Corolla - Carro...',
                }
            ),
            'financier': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite o financiador...'}
            ),
            'installments': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o número de parcelas...',
                }
            ),
            'installments_paid': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o número de parcelas pagas...',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = [('', 'Selecionar...')] + sorted(
            Debt.DEBT_CATEGORIES, key=lambda key: key[1]
        )
