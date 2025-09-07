from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth.base_user import BaseUserManager


class UsuarioManager(BaseUserManager):
  
    def create_user(self, email, password, **extra_fields):
      
        if not email:
            raise ValueError(_('O Email deve ser definido'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # 'set_password' lida com o hashing da senha
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        # Chama o método 'create_user' para evitar duplicação de código
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('medico', 'Medico'),
        ('paciente', 'Paciente'),
    )

    username = None

    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True, null=True, blank=True)
    numero_celular = models.CharField('Número do Celular', max_length=15, null=True, blank=True)
    role = models.CharField('Função', max_length=10, choices=ROLE_CHOICES, default='paciente')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UsuarioManager()
    
    def __str__(self):
        # Define como o objeto será representado como string (ex: no painel de admin)
        return self.email
