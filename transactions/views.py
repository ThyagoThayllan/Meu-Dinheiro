from datetime import datetime
import json

from django.contrib import messages
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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
            error_message = f'Transação de ID <strong>"{pk}"</strong> não existe. Tente novamente.'
            messages.error(request, error_message)

            return redirect('transactions:transactions')

        transaction.delete()

        return redirect('transactions:transactions')


class EditTransaction(TemplateView):
    template_name = 'transactions/edit-transaction.html'

    def get(self, request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            error_message = f'Transação de ID <strong>"{pk}"</strong> não existe. Tente novamente.'
            messages.error(request, error_message)

            return redirect('transactions:transactions')

        form = TransactionForm(instance=transaction)

        return render(request, self.template_name, {'form': form, 'transaction': transaction})

    def post(self, request: HttpRequest, pk: int) -> HttpResponse | HttpResponseRedirect:
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            error_message = f'Transação de ID <strong>"{pk}"</strong> não existe. Tente novamente.'
            messages.error(request, error_message)

            return redirect('transactions:transactions')

        form = TransactionForm(data=request.POST, instance=transaction)

        context = {'form': form, 'transaction': transaction}

        if not form.is_valid():
            return render(request, self.template_name, context)

        form.save()

        messages.success(request, 'Transação editada com sucesso.')

        return render(request, self.template_name, context)


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

        period = request.GET.get('period')

        if period:
            month, year = period.strip().split('-')
        else:
            month, year = datetime.today().strftime('%m-%Y').split('-')

        transactions = Transaction.objects.filter(
            date__month=month, date__year=year, user=request.user
        )

        period = f'{month}-{year}'

        context = {
            'CATEGORIES': json.dumps(dict(Transaction.CATEGORIES)),
            'Transaction': Transaction,
            'form': form,
            'period': period,
            'transactions': transactions,
        }

        return render(request, self.template_name, context)


class TransactionsAjax(View):
    def get(self, request: HttpRequest, period: str) -> JsonResponse:
        if period:
            month, year = period.strip().split('-')
        else:
            month, year = datetime.today().strftime('%m-%Y').split('-')

        transactions = Transaction.objects.filter(
            date__month=month, date__year=year, user=request.user
        ).values()

        return JsonResponse({'data': list(transactions)})
