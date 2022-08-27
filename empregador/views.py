from django.shortcuts import render
from rest_framework import viewsets

from .models import Empregador
from .serializer import EmpregadorSerializer


class EmpregadorViewSet(viewsets.ModelViewSet):
    queryset = Empregador.objects.all()
    serializer_class = EmpregadorSerializer


