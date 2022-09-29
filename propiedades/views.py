import hashlib
import json

from django.core import cache
from rest_framework import generics, viewsets
from rest_framework.response import Response

from propiedades.models import Propiedad
from propiedades.serializers import PropiedadLiteSerializer


class PropiedadesList(generics.ListCreateAPIView):
    queryset = Propiedad.objects.filter(activo=True, publicado=True, foto_perfil__isnull=False)
    serializer_class = PropiedadLiteSerializer

    def get(self, request, *args, **kwargs):
        m = hashlib.md5()
        m.update(str(json.dumps(request.query_params)).encode('utf-8'))
        cache_key = 'propiedades_lista' + m.hexdigest()
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
