from django.db import models

class Empregador(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.IntegerField(unique=True)




