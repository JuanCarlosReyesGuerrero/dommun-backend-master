# Generated by Django 3.2.15 on 2022-09-29 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0002_caracteristicaparqueadero_ciudad_estadopropiedad_numerobano_numerohabitacion_numeroparqueadero_tiemp'),
        ('propiedades', '0011_propiedad_tipo_propiedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='Localizacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='area_construida',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='area_fondo',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='area_privada',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='barrio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.ciudad'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='direccion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='estrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='configuraciones.estrato'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='incluye_administracion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='numero_piso',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='valor_administracion',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='valor_arriendo',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='valor_metro',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]