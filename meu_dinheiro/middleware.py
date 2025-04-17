from typing import Any
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if not request.user.is_authenticated and path not in settings.PUBLIC_URLS:
            messages.error(
                request, 'Você ainda não tem permissão. Por favor, entre na sua conta ou crie uma.'
            )

            return redirect('authentication:login')

        return self.get_response(request)
