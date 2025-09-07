from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioChangeForm, UsuarioCreationForm

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    add_form = UsuarioCreationForm
    
    form = UsuarioChangeForm
    
    model = Usuario

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'cpf', 'numero_celular')}),

        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",  # Adicionamos o nosso campo 'role' aqui
                ),
            },
        ),

        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'first_name', 'last_name', 'cpf', 'numero_celular',
                'role', 'is_staff', 'is_superuser'
            ),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')

    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')

    search_fields = ('email', 'first_name', 'last_name', 'cpf')

    ordering = ('email',)

    readonly_fields = ('date_joined', 'last_login')