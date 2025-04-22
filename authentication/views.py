from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View

from authentication.forms import LoginForm
from authentication.forms import UserForm


User = get_user_model()


class Login(TemplateView):
    template_name = 'authentication/login.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        if not User.objects.filter(email=email).exists():
            form.add_error('email', 'Não existe um usuário com esse e-mail.')

            return render(request, self.template_name, {'form': form})

        if not User.objects.get(email=email).check_password(password):
            form.add_error('password', 'Senha incorreta, tente novamente.')

            return render(request, self.template_name, {'form': form})

        user = authenticate(request, username=email, password=password)

        login(request, user)

        return redirect('dashboard:dashboard')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('authentication:login')


class SignUp(TemplateView):
    template_name = 'authentication/signup.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = UserForm(data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        email = form.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Já existe um usuário com esse e-mail.')
            return render(request, self.template_name, {'form': form})

        user = User.objects.create_user(**form.cleaned_data)

        login(request, user)

        return redirect('dashboard:dashboard')
