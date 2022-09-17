from rest_framework import viewsets, permissions
from .serializers import AgenteSerializers, InmobiliariaSerializers
from .models import Agente, Inmobiliaria


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgenteSerializers

class InmobiliariaViewSet(viewsets.ModelViewSet):
    queryset = Inmobiliaria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InmobiliariaSerializers