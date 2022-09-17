from rest_framework import serializers
from .models import Agente, Inmobiliaria


class AgenteLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = ('id', 'nombre', 'apellido', 'email', 'foto_perfil', 'slug')


class AgentePATCHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = ('id')


class AgenteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class InmobiliariaLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmobiliaria
        fields = ('id', 'slug', 'nit', 'nombre', 'direccion', 'telefono', 'activo', 'created_date')


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
