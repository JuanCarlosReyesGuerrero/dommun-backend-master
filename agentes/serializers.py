from rest_framework import serializers

from propiedades.serializers import PropiedadLiteSerializer
from .models import Agente, Inmobiliaria


class AgenteLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = ('id', 'nombre', 'apellido', 'email', 'foto_perfil', 'slug')


class AgentePATCHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = ('id')


class InmobiliariaLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmobiliaria
        fields = ('id', 'slug', 'nit', 'nombre', 'direccion', 'telefono', 'activo', 'created_date')


class AgenteSerializers(serializers.ModelSerializer):
    inmobiliarias = InmobiliariaLiteSerializer(read_only=True, many=True)
    propiedades = PropiedadLiteSerializer(read_only=True, many=True)

    class Meta:
        model = Agente
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class InmobiliariaPATCHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmobiliaria
        fields = ('id')


class InmobiliariaSerializers(serializers.ModelSerializer):
    agentes = AgenteLiteSerializer(read_only=True, many=True)

    class Meta:
        model = Inmobiliaria
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
