from rest_framework import routers

from agentes.api import AgenteViewSet, InmobiliariaViewSet

router = routers.DefaultRouter()

router.register('api/agentes', AgenteViewSet, 'agentes')
router.register('api/inmobiliarias', InmobiliariaViewSet, 'inmobiliarias')

urlpatterns = router.urls