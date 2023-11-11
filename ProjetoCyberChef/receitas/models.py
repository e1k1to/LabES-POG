from django.db import models


# Create your models here.
class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    calorias = models.IntegerField()
    modopreparo = models.TextField()
    carboidrato = models.FloatField()
    proteina = models.FloatField()
    fibra = models.FloatField()
    sodio = models.FloatField()
    foto = models.ImageField(upload_to='receitas/fotos/')
    acessos = models.PositiveIntegerField(default=0)

    @classmethod
    def top3_acessadas(cls):
        return cls.objects.order_by('-acessos')[:2]

    def __str__(self):
        return self.titulo


class MensagemContato(models.Model):
    motivo = models.CharField(max_length=255)
    email = models.EmailField()
    descricao = models.TextField()

    def __str__(self):
        return self.motivo
