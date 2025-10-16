from django import forms
from django.forms import ModelForm
from .models import Veiculo

class FormularioVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        exclude = []
        widgets = {
            'marca': forms.Select(attrs={
                'class': 'form-control form-select',
                'placeholder': 'Selecione a marca'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o modelo do veículo',
                'maxlength': 100
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o ano do veículo',
                'min': 1900,
                'max': 2030
            }),
            'cor': forms.Select(attrs={
                'class': 'form-control form-select',
                'placeholder': 'Selecione a cor'
            }),
            'combustivel': forms.Select(attrs={
                'class': 'form-control form-select',
                'placeholder': 'Selecione o tipo de combustível'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
        labels = {
            'marca': 'Marca do Veículo',
            'modelo': 'Modelo',
            'ano': 'Ano de Fabricação',
            'cor': 'Cor do Veículo',
            'combustivel': 'Tipo de Combustível',
            'foto': 'Foto do Veículo'
        }
        help_texts = {
            'marca': 'Selecione a marca do fabricante',
            'modelo': 'Digite o modelo específico do veículo',
            'ano': 'Ano de fabricação do veículo',
            'cor': 'Escolha a cor predominante do veículo',
            'combustivel': 'Tipo de combustível que o veículo utiliza',
            'foto': 'Faça upload de uma foto do veículo (opcional)'
        }