from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from polaris.common.filters import FilterSet
from polaris.common.views import ModelViewSet
from rest_framework.filters import OrderingFilter

from movie.models import MovieModel
from movie.serializer import MovieSerializer


class MovieFilter(FilterSet):
    movi_character_id = filters.ChoiceFilter(('first'), ('3fa85f64-5717-4562-b3fc-2c963f66afa6'))
    movi_director = filters.ChoiceFilter(lookup_expr='eq')
    movi_producers = filters.ChoiceFilter(lookup_expr='eq')
    movi_planet_id = filters.CharFilter(lookup_expr='eq')

    class Meta:
        model = MovieModel
        fields = [
            'movi_character_id',
            'movi_director',
            'movi_producers',
            'movi_planet_id'
        ]


class MovieViewSet(ModelViewSet):
    queryset = MovieModel.objects
    serializer_class = MovieSerializer
    lookup_field = 'movi_id'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ['movi_premiere']
