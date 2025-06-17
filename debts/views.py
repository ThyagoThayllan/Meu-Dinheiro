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
        return render(request, self.template_name)
