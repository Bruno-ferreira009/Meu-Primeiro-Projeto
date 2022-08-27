from django.db import models

from empregador.models import Empregador


class Vaga(models.Model):
    nome = models.CharField(max_length=100)
    qualificacao = models.CharField(max_length=100)
    empregador = models.ForeignKey(Empregador, on_delete=models.CASCADE)
    salario = models.IntegerField()





