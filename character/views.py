from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from polaris.common.filters import FilterSet
from polaris.common.views import ModelViewSet

from character.models import CharacterModel
from character.serializer import CharacterSerializer


class CharacterFilter(FilterSet):
    char_planet_home = filters.CharFilter(lookup_expr='eq')
    char_planet_id = filters.UUIDFilter(lookup_expr='eq')
    char_species = filters.CharFilter(lookup_expr='eq')

    class Meta:
        model = CharacterModel
        fields = [
            'char_planet_home',
            'char_planet_id',
            'char_species'
        ]


class CharacterViewSet(ModelViewSet):
    queryset = CharacterModel.objects
    serializer_class = CharacterSerializer
    lookup_field = 'char_id'
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter
