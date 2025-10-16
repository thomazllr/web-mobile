from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', NovoVeiculo.as_view(), name='novo-veiculo'),
    path('fotos/<str:filename>/', FotoVeiculo.as_view(), name='foto-veiculo'),
]