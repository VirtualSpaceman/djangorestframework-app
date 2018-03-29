from .serializer import clienteSerializer, produtoSerializer, vendaSerializer, maisVendidosSerializer, melhoresDoMesSerializer
from .models import Cliente, Produto, Venda, MaisVendidos, MelhoresDoMes
from . import factories

from rest_framework import viewsets, permissions

from datetime import date
import operator
from collections import Counter

class clienteListView(viewsets.ModelViewSet): 
    print(factories.ClienteFactory())
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ProdutoView(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = produtoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class VendaView(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = vendaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class MaisVendidosView(viewsets.ReadOnlyModelViewSet):
    vendas, produtos = list(Venda.objects.all()), list(Produto.objects.all())
    maisVendidos = dict()
    #recupera os produtos mais vendidos no mes
    if len(vendas) > 0: 
        '''
        Essa parte pega todos os produtos existentes do bando de dados 
        e faz-se um dicionario que mapeia prod_id: qtd
        '''
        for item in list(Produto.objects.all()):
            maisVendidos[item.id] = 0
        
        for venda in vendas:
            listaProdutos = venda.produtos.all()
            for elem in listaProdutos:
                maisVendidos[elem.id] +=1
        
        maisVendidos = sorted(maisVendidos.items(), key=operator.itemgetter(1), reverse=True)
    
    check = MaisVendidos.objects.all().count()
    if check:
        obj = MaisVendidos.objects.get(id=1)
        obj.descricao = str(maisVendidos)
        obj.save()
    else:
        entry = MaisVendidos(descricao = str(maisVendidos), qtd = 1)
        entry.save()
    
    queryset = MaisVendidos.objects.all()
    serializer_class = maisVendidosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )     

class MelhoresDoMesView(viewsets.ReadOnlyModelViewSet):
    
     #Recupera os melhores vendedores do mes
    meses = ['01', '02' ,'03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    start, end = date(2018, 1, 1), date(2018, 12, 30)
    vendas = list(Venda.objects.all())
    vendedores = list(Venda.objects.values('vendedor').distinct())
    melhoresVendedores = dict() #levando apenas em conta o ano de 2018

    for mes in meses:
        z = []
        for venda in vendas:
            if str(venda.data)[5:7] == mes:
                z.append(venda.vendedor)
        melhoresVendedores[mes] = dict(Counter(z).most_common(1)) #pega o que mais vendeu no mês
        print(melhoresVendedores[mes])

    check = MelhoresDoMes.objects.all().count()
    if check:
        obj = MelhoresDoMes.objects.get(id=1)
        obj.vendasMes = str(melhoresVendedores)
        obj.save()
    else:
        entry = MelhoresDoMes(ano = '2018', vendasMes = str("{1:0},{2:0},{3:0}, {4:0},{5:0},{6:0},{7:0},{8:0},{9:0},{10:0},{11:0},{12:0}"))
        entry.save()
    
    queryset = MelhoresDoMes.objects.all()
    serializer_class = melhoresDoMesSerializer