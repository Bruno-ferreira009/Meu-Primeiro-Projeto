from rest_framework import serializers

from empregador.serializer import EmpregadorSerializer


class VagaSerializer(serializers.Serializer):
    nome = serializers.CharField()
    qualificacao = serializers.CharField()
    empregador = EmpregadorSerializer()
    salario = serializers.IntegerField()