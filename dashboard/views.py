from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'user': 'Thyago Thayllan'})
