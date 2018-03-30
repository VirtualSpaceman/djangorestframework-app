from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length = 50)
    preco = models.FloatField()

class Venda(models.Model):
    clienteId = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    data = models.DateField()
    vendedor = models.CharField(max_length = 30)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.produtos

class MaisVendidos(models.Model):
    descricao = models.CharField(max_length = 100)
    qtd = models.IntegerField()

class MelhoresDoMes(models.Model):
    ano = models.CharField(max_length = 4)
    vendasMes = models.CharField(max_length = 200)

class VendasMensais(models.Model):
    ano = models.CharField(max_length = 4)
    meses = models.CharField(max_length = 200)
