from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm, ContatoForm
from django.views.generic import ListView


# Create your views here.
def inicio(request):
    receitaspopulares = Receita.top3_acessadas()
    return render(request, 'receitas/inicio.html', {'receitas_populares': receitaspopulares})


def detalhe_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'receitas/detalhe-receita.html', {'receita': receita})


def todas_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/todas-receitas.html', {'receitas': receitas})


def enviar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ReceitaForm()
    return render(request, 'receitas/enviar-receita.html', {'form': form})


def receitas_populares(request):
    receitas = Receita.objects.all()[:2]  # Pega as duas primeiras receitas
    return render(request, 'receitas/inicio.html', {'receitas': receitas})


class ReceitaListView(ListView):
    model = Receita
    template_name = 'receitas/resultados_pesquisa.html'
    context_object_name = 'receitas'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar as receitas com base nos parâmetros da URL
        ingredientes_param = self.request.GET.get('ingredientes', None)
        calorias_max = self.request.GET.get('calorias', None)
        carboidratos_max = self.request.GET.get('carboidrato', None)
        proteina_max = self.request.GET.get('proteina', None)
        fibras_max = self.request.GET.get('fibra', None)
        sodio_max = self.request.GET.get('sodio', None)

        if ingredientes_param:
            # Divida os ingredientes por vírgulas
            ingredientes = [ingrediente.strip() for ingrediente in ingredientes_param.split(',')]

            # Use o campo 'ingredientes' do modelo Receita para filtrar
            # Utilize '__icontains' se quiser uma busca case-insensitive
            # Utilize '__contains' se quiser uma busca case-sensitive
            queryset = queryset.filter(ingredientes__icontains=ingredientes[0])

            # Adicione lógica para filtrar por outros ingredientes, se necessário
            for ingrediente in ingredientes[1:]:
                queryset = queryset.filter(ingredientes__icontains=ingrediente)

        if calorias_max is not None and calorias_max != '':
            queryset = queryset.filter(calorias__lte=calorias_max)

        if carboidratos_max is not None and carboidratos_max != '':
            queryset = queryset.filter(carboidrato__lte=carboidratos_max)

        if proteina_max is not None and proteina_max != '':
            queryset = queryset.filter(proteina__lte=proteina_max)

        if fibras_max is not None and fibras_max != '':
            queryset = queryset.filter(fibra__lte=fibras_max)

        if sodio_max and sodio_max.isdigit():
            queryset = queryset.filter(sodio__lte=sodio_max)

        return queryset


def fale_conosco(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receita-inicio')
    else:
        form = ContatoForm()

    return render(request, 'receitas/fale-conosco.html', {'form': form})
