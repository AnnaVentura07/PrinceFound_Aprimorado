from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('dicas/', views.dicas, name='dicas'),
    path('carrinho/', views.exibir_carrinho, name='exibir_carrinho'),
    path('carrinho/add/<int:id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]

