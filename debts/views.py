from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class Debts(TemplateView):
    template_name = 'debts/debts.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
