from rest_framework import serializers

class EmpregadorSerializer(serializers.Serializer):
    nome = serializers.CharField()
    cnpj = serializers.IntegerField()