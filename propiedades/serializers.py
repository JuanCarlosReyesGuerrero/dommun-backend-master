from rest_framework import serializers

from propiedades.models import Propiedad


class PropiedadLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        #fields = ('id', 'activo', 'created_date')
        fields = '__all__'