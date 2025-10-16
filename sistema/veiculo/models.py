from django.db import models
from .consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEL

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEL)
    foto = models.ImageField(upload_to='veiculo/fotos', null=True, blank=True)