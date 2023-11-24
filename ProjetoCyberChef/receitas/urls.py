from django.urls import path
from . import views
from .views import ReceitaListView


urlpatterns = [
    path('', views.inicio, name="receita-inicio"),
    path('receita/<int:receita_id>/', views.detalhe_receita, name='detalhe_receita'),
    path('todas/', views.todas_receitas, name='todas_receitas'),
    path('enviar/', views.enviar_receita, name='enviar'),
    path('contato/', views.fale_conosco, name='contato'),
    path('filtrar/', ReceitaListView.as_view(), name='filtrar'),
]


