from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm, ContatoForm


# Create your views here.
def inicio(request):
    receitas_populares = Receita.top3_acessadas()
    return render(request, 'receitas/inicio.html', {'receitas_populares': receitas_populares})


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



def filtar_receitas(request):
    return render(request, 'receitas/index.html')


def fale_conosco(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receita-inicio')
    else:
        form = ContatoForm()

    return render(request, 'receitas/fale-conosco.html', {'form': form})
