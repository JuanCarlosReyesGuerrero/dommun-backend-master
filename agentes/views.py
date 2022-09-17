import hashlib
import json

from django.core import cache
from rest_framework import generics, viewsets
from rest_framework.response import Response

from agentes.models import Agente, Inmobiliaria
from agentes.serializers import AgenteSerializers, AgentePATCHSerializer, AgenteLiteSerializer, \
    InmobiliariaLiteSerializer


class AgentesList(generics.ListCreateAPIView):
    queryset = Agente.objects.exclude(foto_perfil='').filter(activo=True, publicado=True, foto_perfil__isnull=False)
    serializer_class = AgenteLiteSerializer

    def get(self, request, *args, **kwargs):
        m = hashlib.md5()
        m.update(str(json.dumps(request.query_params)).encode('utf-8'))
        cache_key = 'agentes_lista' + m.hexdigest()
        # time to live in seconds
        cache_time = 3600
        qs = cache.get(cache_key)
        if not qs:
            rep = self.list(request, *args, **kwargs)
            qs = json.dumps(rep.data)
            cache.set(cache_key, qs, cache_time)
        else:
            rep = Response(json.loads(qs))
        return rep

class InmobiliariasList(generics.ListCreateAPIView):
    queryset = Inmobiliaria.objects.filter(activo=True, publicado=True, foto_perfil__isnull=False)
    serializer_class = InmobiliariaLiteSerializer

    def get(self, request, *args, **kwargs):
        m = hashlib.md5()
        m.update(str(json.dumps(request.query_params)).encode('utf-8'))
        cache_key = 'inmobiliarias_lista' + m.hexdigest()
        # time to live in seconds
        cache_time = 3600
        qs = cache.get(cache_key)
        if not qs:
            rep = self.list(request, *args, **kwargs)
            qs = json.dumps(rep.data)
            cache.set(cache_key, qs, cache_time)
        else:
            rep = Response(json.loads(qs))
        return rep


class AgentesDetail(generics.RetrieveUpdateAPIView):
    queryset = Agente.objects.exclude(foto_perfil='').filter(activo=True, publicado=True, foto_perfil__isnull=False)
    serializer_class = AgenteSerializers

    def patch(self, request, *args, **kwargs):
        self.serializer_class = AgentePATCHSerializer
        return self.partial_update(request, *args, **kwargs)


class AgentesRetrive(viewsets.ReadOnlyModelViewSet):
    queryset = Agente.objects.exclude(foto_perfil='').filter(activo=True, publicado=True, foto_perfil__isnull=False)
    serializer_class = AgenteSerializers
