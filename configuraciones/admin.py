from django.contrib import admin

from configuraciones.models import Estrato,TipoOferta, TipoPropiedad, EstadoPropiedad, Ciudad, TipoParqueadero, TiempoConstruido, \
    CaracteristicaParqueadero, NumeroBano, NumeroHabitacion, NumeroParqueadero

admin.site.register(Estrato)
admin.site.register(TipoOferta)
admin.site.register(TipoPropiedad)
admin.site.register(EstadoPropiedad)
admin.site.register(Ciudad)
admin.site.register(TiempoConstruido)
admin.site.register(TipoParqueadero)
admin.site.register(CaracteristicaParqueadero)
admin.site.register(NumeroBano)
admin.site.register(NumeroHabitacion)
admin.site.register(NumeroParqueadero)
