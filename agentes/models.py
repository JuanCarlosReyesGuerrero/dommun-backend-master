from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Inmobiliaria(models.Model):
    slug = models.SlugField(unique=False, null=False, blank=False, max_length=100)
    nit = models.CharField(null=True, blank=True, max_length=12)
    nombre = models.CharField(null=True, blank=True, max_length=60)
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(null=True, blank=True, max_length=30)
    activo = models.BooleanField(null=False, default=True, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Agente(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        unique=True,
        related_name='agente',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(null=False, blank=True)
    nombre = models.CharField(max_length=120, null=True, blank=True)
    apellido = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    # foto_perfil = models.ImageField(upload_to=upload_foto_agente, blank=True, null=True)
    foto_perfil = models.CharField(max_length=120, null=True, blank=True)
    descripcion_perfil = models.TextField(null=True, blank=True)
    celular = models.CharField(null=True, blank=True, max_length=80)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    twitter = models.CharField(max_length=120, null=True, blank=True)
    linkedin = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=120, null=True, blank=True)
    activo = models.BooleanField(null=False, default=True, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    inmobiliaria = models.ForeignKey(Inmobiliaria, null=True, blank=True, related_name='agentes',
                                     on_delete=models.CASCADE)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre + " " + self.apellido

    def save(self, *args, **kwargs):
        from django.contrib.auth.models import Group

        if self.activo:
            if self.user is None:
                user = User.objects.create_user(username=self.slug,
                                                email=self.email,
                                                first_name=self.nombre,
                                                last_name=self.apellido, password='FAJSflk-ehqKLY570TY34P87')
                g = Group.objects.get(name='agentes')
                g.user_set.add(user)
                self.user = user
        super(Agente, self).save(*args, **kwargs)

    class Meta:
        ordering = ('nombre', 'apellido')
