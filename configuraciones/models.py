from django.db import models


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

    class Meta:
        verbose_name_plural = "Caracteristica Parqueaderos"
        verbose_name = "Caracteristica Parqueadero"


class NumeroBano(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Número Baños"
        verbose_name = "Número Baños"


class NumeroHabitacion(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Número Habitaciones"
        verbose_name = "Número Habitación"


class NumeroParqueadero(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    activo = models.BooleanField(null=False, default=True, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Número Parqueaderos"
        verbose_name = "Número Parqueadero"
