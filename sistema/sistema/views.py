from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Login(View):
    """
    Class based View para autenticação de usuários.
    """

    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)