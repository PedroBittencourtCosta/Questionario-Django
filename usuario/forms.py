from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    """
    Um formulário para criar novos utilizadores. Inclui todos os campos necessários
    e lida com a validação e hashing da palavra-passe.
    """
    class Meta(UserCreationForm.Meta):
        model = Usuario
        # Os campos aqui são os que aparecerão no formulário de CRIAÇÃO.
        # Note que 'email' está aqui, e 'username' não está.
        fields = (
            'email', 'first_name', 'last_name', 'cpf',
            'numero_celular', 'role', 'is_staff', 'is_superuser'
        )
    
    def is_valid(self):
        """
        Sobrescrevemos o método is_valid para depuração.
        Se o formulário for inválido, imprimimos os erros no console.
        """
        valid = super().is_valid()
        if not valid:
            print("--- INÍCIO DOS ERROS DE DEPURAÇÃO DO FORMULÁRIO ---")
            # O .as_json() formata os erros de uma maneira fácil de ler.
            print(self.errors.as_json())
            print("--- FIM DOS ERROS DE DEPURAÇÃO DO FORMULÁRIO ---")
        return valid
    
    
class UsuarioChangeForm(UserChangeForm):
    """
    Um formulário para atualizar utilizadores existentes. A principal diferença
    é que não lida diretamente com a palavra-passe da mesma forma que o CreationForm.
    """
    class Meta:
        model = Usuario
        # Os campos aqui são os que aparecerão no formulário de EDIÇÃO.
        fields = ('email', 'first_name', 'last_name', 'cpf', 'numero_celular', 'role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

