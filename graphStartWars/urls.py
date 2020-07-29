# from django.urls import path, include
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework.routers import SimpleRouter
#
# from character.views import CharacterViewSet
# from movie.views import MovieViewSet
# from planet.views import PlanetViewSet
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Graph Start Wars",
#         default_version="v1",
#         description="Aplicación para fanaticos de Star Wars"
#     ),
#     public=True
# )
# router = SimpleRouter()
# router.register(r'character', CharacterViewSet)
# router.register(r'movie', MovieViewSet)
# router.register(r'planet', PlanetViewSet)
#
# urlpatterns = [
#     path('star_wars/api/', include(router.urls)),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
# ]

from django.urls import path
from graphene_django.views import GraphQLView

from character import schema

urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema, graphiql=True)),
]
