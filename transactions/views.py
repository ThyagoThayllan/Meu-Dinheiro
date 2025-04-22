from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Transaction
from .forms import TransactionForm


class DeleteTransaction(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            error_message = (
                f'Transação de ID <strong>"{pk}"</strong> não existe. Tente novamente.'
            )
            messages.error(request, error_message)

            return redirect('transactions:transactions')

        transaction.delete()

        return redirect('transactions:transactions')


class NewTransaction(View):
    def post(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        form = TransactionForm(data=request.POST)

        if not form.is_valid():
            return render(request, 'transactions/transactions.html', {'form': form})

        Transaction.objects.create(**form.cleaned_data, user=request.user)

        return redirect('transactions:transactions')


class Transactions(TemplateView):
    template_name = 'transactions/transactions.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = TransactionForm()

        transactions = Transaction.objects.filter(user=request.user)

        context = {'form': form, 'transactions': transactions}

        return render(request, self.template_name, context)
