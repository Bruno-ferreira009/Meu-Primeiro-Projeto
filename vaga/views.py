from django.shortcuts import render
from rest_framework import viewsets

from .models import Vaga
from .serializer import VagaSerializer


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

