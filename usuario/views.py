from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UsuarioRegisterForm

# Create your views here.

class SignUpView(generic.CreateView):
    # Usa o nosso formulário personalizado
    form_class = UsuarioRegisterForm
    
    # Em caso de sucesso no cadastro, redireciona o utilizador para a página de login
    # 'reverse_lazy' é usado para que a URL seja resolvida apenas quando necessário
    success_url = reverse_lazy('login')
    
    # O template HTML que será usado para renderizar esta página
    template_name = 'register_page.html'