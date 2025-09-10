from django.urls import path
# Importa a LoginView e LogoutView prontas do Django
from django.contrib.auth.views import LoginView, LogoutView

# Importa a sua view de cadastro que já tínhamos criado
# from .views import SignUpView

urlpatterns = [
    # URL para a página de cadastro, que usa a sua view personalizada.
    # path('signup/', SignUpView.as_view(), name='signup'),

    # URL para a página de login. É aqui que a magia acontece.
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),

    # URL para a funcionalidade de logout. Também usa uma view pronta.
    path('logout/', LogoutView.as_view(), name='logout'),
]