from django.contrib import messages
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .forms import DebtForm
from .models import Debt


class Debts(TemplateView):
    template_name = 'debts/debts.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        debts = Debt.objects.filter(user=request.user)

        form = DebtForm()

        context = {'debts': debts, 'form': form}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = DebtForm(data=request.POST)

        if not form.is_valid():
            debts = Debt.objects.filter(user=request.user)

            return render(request, self.template_name, {'debts': debts, 'form': form})

        if form.cleaned_data['installments'] == form.cleaned_data['installments_paid']:
            form.cleaned_data['is_paid'] = True

        Debt.objects.create(**form.cleaned_data, user=request.user)

        return redirect('debts:debts')


class DebtDelete(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponseRedirect:
        try:
            debt = Debt.objects.get(pk=pk)
        except Debt.DoesNotExist:
            error_message = f'Dívida de ID <strong>"{pk}"</strong> não existe. Tente novamente.'
            messages.error(request, error_message)

            return redirect('debts:debts')

        debt.delete()

        return redirect('debts:debts')
