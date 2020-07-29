import graphene
from graphene_django import DjangoObjectType

from character.models import CharacterModel


class CharacterType(DjangoObjectType):
    class Meta:
        model = CharacterModel


class Query(graphene.ObjectType):
    heroes = graphene.List(CharacterType)

    def resolve_characters(self, info, **kwargs):
        return CharacterModel.objects.all()
