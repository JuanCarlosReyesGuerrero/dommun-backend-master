# Generated by Django 3.2.15 on 2022-09-29 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0002_caracteristicaparqueadero_ciudad_estadopropiedad_numerobano_numerohabitacion_numeroparqueadero_tiemp'),
        ('propiedades', '0010_propiedad_tipo_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.tipopropiedad'),
        ),
    ]