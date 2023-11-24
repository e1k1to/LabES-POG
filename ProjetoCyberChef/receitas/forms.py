from django import forms
from .models import Receita, MensagemContato


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'calorias', 'modopreparo', 'carboidrato', 'proteina', 'fibra', 'sodio',
                  'foto']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['motivo', 'email', 'descricao']


class FiltroReceitaForm(forms.Form):
    calorias = forms.FloatField(required=False)
    carboidrato = forms.FloatField(required=False)
    proteina = forms.FloatField(required=False)
    fibra = forms.FloatField(required=False)
    sodio = forms.FloatField(required=False)
