import factory
from . import models

class ClienteFactory(factory.Factory):
    class Meta:
        model = models.Cliente
    
    nome = factory.Faker('name')
