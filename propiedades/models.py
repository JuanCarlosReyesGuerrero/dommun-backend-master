from django.db import models
from django.utils import timezone

from configuraciones.models import Estrato


class Propiedad(models.Model):
    valor_venta = models.FloatField(null=False, blank=False)
    valor_arriendo = models.FloatField(null=False, blank=False)
    incluye_administracion = models.BooleanField(null=False, default=False)
    valor_administracion = models.FloatField(null=False, blank=False)
    valor_metro = models.FloatField(null=False, blank=False)

    Estrato = models.ForeignKey(Estrato, null=True, blank=True, related_name='propiedades',
                                on_delete=models.CASCADE)
    activo = models.BooleanField(null=False, default=True, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.estrato

    class Meta:
        verbose_name_plural = "Propiedades"
        verbose_name = "Propiedad"
