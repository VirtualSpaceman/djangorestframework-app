from rest_framework import serializers
from .models import *

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']

class produtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'descricao', 'preco']

class vendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'clienteId', 'data', 'vendedor', 'produtos']

class maisVendidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaisVendidos
        fields = ['descricao']

class melhoresDoMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MelhoresDoMes
        fields = ['ano', 'vendasMes']

class vendasMensaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendasMensais
        fields = ['ano', 'meses']
        