from django.forms import ModelForm


from .models import Cliente

class FormClientes(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'age', 'endereco', 'salario', 'bio', 'imagem']