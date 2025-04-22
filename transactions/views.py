from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Transactions(TemplateView):
    template_name = 'transactions/transactions.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = TransactionForm()

        transactions = Transaction.objects.filter(user=request.user)

        context = {'form': form, 'transactions': transactions}

        return render(request, self.template_name, context)
