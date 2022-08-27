from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    qualificacao = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome

