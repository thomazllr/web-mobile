from django.shortcuts import render, redirect
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.views.generic import ListView
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/veiculo.html'


class NovoVeiculo(LoginRequiredMixin, View):
    def get(self, request):
        form = FormularioVeiculo()
        context = {
            'form': form,
        }
        return render(request, 'veiculo/novo.html', context)
    
    def post(self, request):
        form = FormularioVeiculo(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                veiculo = form.save()
                return redirect('listar-veiculos')
                
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar veículo: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
        
        context = {
            'form': form,
        }
        return render(request, 'veiculo/novo.html', context)

class FotoVeiculo(View):
    def get(self, request, filename):
        try:
            veiculo = Veiculo.objects.filter(foto=f'veiculo/fotos/{filename}').first()
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada.")
        except Exception as e:
            raise Http404(f"Erro ao carregar foto: {str(e)}")