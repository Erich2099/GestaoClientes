from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Cliente


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ClientesListView(ListView):
    template_name = 'core/clientes_list.html'
    model = Cliente


class ClienteDetailtView(DetailView):
    model = Cliente
    template_name = 'core/clientes_detail.html'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'core/clientes_add.html'
    fields = ('nome', 'age', 'endereco', 'salario', 'bio', 'imagem')
    success_url = reverse_lazy('lista')



class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'core/clientes_update.html'
    fields = ('nome', 'age', 'endereco', 'salario', 'bio', 'imagem')

    def get_success_url(self):
        return reverse_lazy('lista')



class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'core/clientes_delete.html'
    success_url = reverse_lazy('lista')
