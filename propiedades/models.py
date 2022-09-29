from django.db import models
from django.utils import timezone

from agentes.models import Agente
from configuraciones.models import Estrato, TipoOferta, TipoPropiedad, Ciudad, TiempoConstruido, NumeroHabitacion, \
    NumeroBano, NumeroParqueadero, TipoParqueadero, CaracteristicaParqueadero, EstadoPropiedad


class Propiedad(models.Model):
    matricula_inmobiliaria = models.CharField(null=True, blank=True, max_length=100)
    tipo_oferta = models.ForeignKey(TipoOferta, null=True, blank=True, related_name='propiedades',
                                    on_delete=models.CASCADE)
    tipo_propiedad = models.ForeignKey(TipoPropiedad, null=True, blank=True, related_name='propiedades',
                                       on_delete=models.CASCADE)
    valor_venta = models.FloatField(null=False, blank=False)
    valor_arriendo = models.FloatField(null=False, blank=False)
    incluye_administracion = models.BooleanField(null=False, default=False)
    valor_administracion = models.FloatField(null=False, blank=False)
    valor_metro = models.FloatField(null=False, blank=False)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, related_name='propiedades',
                               on_delete=models.CASCADE)
    direccion = models.TextField(null=True, blank=True)
    barrio = models.CharField(null=True, blank=True, max_length=100)
    Localizacion = models.CharField(null=True, blank=True, max_length=100)
    estrato = models.ForeignKey(Estrato, null=True, blank=True, related_name='propiedades',
                                on_delete=models.CASCADE)
    area_privada = models.FloatField(null=False, blank=False)
    area_construida = models.FloatField(null=False, blank=False)
    area_fondo = models.FloatField(null=False, blank=False)
    numero_piso = models.IntegerField(null=False, blank=False)
    tiempo_construido = models.ForeignKey(TiempoConstruido, null=True, blank=True, related_name='propiedades',
                                          on_delete=models.CASCADE)
    numero_habitacion = models.ForeignKey(NumeroHabitacion, null=True, blank=True, related_name='propiedades',
                                          on_delete=models.CASCADE)
    numero_bano = models.ForeignKey(NumeroBano, null=True, blank=True, related_name='propiedades',
                                    on_delete=models.CASCADE)
    numero_parqueadero = models.ForeignKey(NumeroParqueadero, null=True, blank=True, related_name='propiedades',
                                           on_delete=models.CASCADE)
    tipo_parqueadero = models.ForeignKey(TipoParqueadero, null=True, blank=True, related_name='propiedades',
                                         on_delete=models.CASCADE)
    caracteristica_parqueadero = models.ForeignKey(CaracteristicaParqueadero, null=True, blank=True,
                                                   related_name='propiedades',
                                                   on_delete=models.CASCADE)
    caracteristicas = models.TextField(null=True, blank=True)
    video = models.TextField(null=True, blank=True, max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    anio_construccion = models.IntegerField(null=False, blank=False)
    estado_propiedad = models.ForeignKey(EstadoPropiedad, null=True, blank=True,
                                         related_name='propiedades',
                                         on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, null=True, blank=True,
                               related_name='propiedades',
                               on_delete=models.CASCADE)
    activo = models.BooleanField(null=False, default=True, blank=False)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.matricula_inmobiliaria

    def owner(self):
        return self.agente.user

    class Meta:
        verbose_name_plural = "Propiedades"
        verbose_name = "Propiedad"
