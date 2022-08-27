from rest_framework import serializers

from empregador.serializer import EmpregadorSerializer


class PessoaSerializer(serializers.Serializer):
    nome = serializers.CharField()
    qualificacao = serializers.CharField()
    cpf = serializers.IntegerField()
