from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class Persons(TemplateView):
    template_name = 'persons/persons.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
