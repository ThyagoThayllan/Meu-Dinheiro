from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView

from authentication.forms import LoginForm
from authentication.forms import SignUpForm
from authentication.models import User


class Login(TemplateView):
    template_name = 'authentication/login.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=password, username=email)
        breakpoint()
        return redirect('dashboard:dashboard')


class SignUp(TemplateView):
    template_name = 'authentication/signup.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': SignUpForm})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm(data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        return redirect('dashboard:dashboard')
