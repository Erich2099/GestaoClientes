from django.urls import path

from .views import (
    IndexView,
    ClientesListView,
    ClienteDetailtView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lista/', ClientesListView.as_view(), name='lista'),
    path('adicionar', ClienteCreateView.as_view(), name='cliente-adicionar'),
    path('lista/<int:pk>/', ClienteDetailtView.as_view(), name='cliente-detalhe'),
    path('lista/atualizar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-atualizar'),
    path('lista/<int:pk>/deletar/', ClienteDeleteView.as_view(), name='cliente-apagar'),
]
