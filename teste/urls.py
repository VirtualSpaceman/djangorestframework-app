from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', views.clienteListView)
router.register('produtos', views.ProdutoView)
router.register('vendas', views.VendaView)
router.register('maisvendidos', views.MaisVendidosView)
router.register('melhoresmeses', views.MelhoresDoMesView)
router.register('vendasmensais', views.VendasMensaisView)

urlpatterns = [
    path('', include(router.urls))
]