from rest_framework import serializers
from .models import Produto, Estoque, Categoria

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    estoque = EstoqueSerializer(read_only=True) 
    categoria_nome = serializers.ReadOnlyField(source='categoria.nome')

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'marca', 'preco', 'categoria', 'categoria_nome', 'descricao', 'estoque']