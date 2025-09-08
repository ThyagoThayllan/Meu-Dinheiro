from datetime import datetime

from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse

from transactions.models import Transaction


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
