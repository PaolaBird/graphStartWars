from polaris.common.views import ModelViewSet

from planet.models import PlanetModel
from planet.serializer import PlanetSerializer


class PlanetViewSet(ModelViewSet):
    queryset = PlanetModel.objects
    serializer_class = PlanetSerializer
    lookup_field = 'plan_id'
