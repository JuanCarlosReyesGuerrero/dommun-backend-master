from django.db import models
from django.utils import timezone


class Estrato(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Estratos"
        verbose_name = "Estrato"


class TipoOferta(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipo Ofertas"
        verbose_name = "Tipo Oferta"


class TipoPropiedad(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipo Propiedades"
        verbose_name = "Tipo Propiedad"


class EstadoPropiedad(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Estado Propiedades"
        verbose_name = "Estado Propiedad"


class Ciudad(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"
        verbose_name = "Ciudad"


class TiempoConstruido(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tiempo Construidos"
        verbose_name = "Tiempo Construido"


class TipoParqueadero(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipo Parqueaderos"
        verbose_name = "Tipo Parqueadero"


class CaracteristicaParqueadero(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre


class NumeroBano(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre


class NumeroHabitacion(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre


class NumeroParqueadero(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre


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
