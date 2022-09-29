# Generated by Django 3.2.15 on 2022-09-29 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
        ('configuraciones', '0002_caracteristicaparqueadero_ciudad_estadopropiedad_numerobano_numerohabitacion_numeroparqueadero_tiemp'),
        ('propiedades', '0012_auto_20220928_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='agente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='agentes.agente'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='anio_construccion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='caracteristica_parqueadero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.caracteristicaparqueadero'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='caracteristicas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='estado_propiedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.estadopropiedad'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='numero_bano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.numerobano'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='numero_habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.numerohabitacion'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='numero_parqueadero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.numeroparqueadero'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tiempo_construido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.tiempoconstruido'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipo_parqueadero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.tipoparqueadero'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='video',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]