import uuid

from polaris.common.serializers import AuditorySerializer, CustomDateField, CustomTimeField
from polaris.common.utilities import Constants
from rest_framework import serializers

from character.serializer import CharacterSerializer
from movie.models import MovieModel
from planet.serializer import PlanetSerializer


class MovieSerializer(AuditorySerializer):
    movi_id = serializers.UUIDField(required=False, default=uuid.uuid4, read_only=True)
    movi_name = serializers.CharField(required=True)
    movi_opening_text = serializers.CharField(required=True)
    movi_character_id = serializers.ListField(required=True, child=serializers.UUIDField())
    movi_character = serializers.ListField(required=False, allow_empty=True, allow_null=True,
                                           child=serializers.JSONField())
    movi_director = serializers.ListField(required=True, child=serializers.CharField())
    movi_producers = serializers.ListField(required=True, child=serializers.CharField())
    movi_soundtrack = serializers.ListField(required=True, child=serializers.CharField())
    movi_premiere = CustomDateField(required=True, format=Constants.FORMAT_DATE)
    movi_duration = CustomTimeField(required=True, format=Constants.FORMAT_TIME)
    movi_planet_id = serializers.ListField(required=True, child=serializers.UUIDField())
    movi_planet = serializers.ListField(required=False, allow_empty=True, allow_null=True,
                                        child=serializers.JSONField())

    class Meta:
        model = MovieModel
        fields = '__all__'

    def create(self, validated_data):

        characters, planets = self.character_planet(validated_data)
        return MovieModel(movi_id=uuid.uuid4(),
                          movi_name=validated_data['movi_name'],
                          movi_opening_text=validated_data['movi_opening_text'],
                          movi_character_id=validated_data['movi_character_id'],
                          movi_character=characters,
                          movi_director=validated_data['movi_director'],
                          movi_producers=validated_data['movi_producers'],
                          movi_soundtrack=validated_data['movi_soundtrack'],
                          movi_premiere=validated_data['movi_premiere'],
                          movi_duration=validated_data['movi_duration'],
                          movi_planet_id=validated_data['movi_planet_id'],
                          movi_planet=planets)

    def character_planet(self, instance):
        characters = []
        planets = []
        for character in instance['movi_character_id']:
            characters.append(CharacterSerializer.get_character(character))
        instance['movi_character'] = characters

        for planet in instance['movi_planet_id']:
            planets.append(PlanetSerializer.get_planet(planet))
        instance['movi_planet'] = planets

        return characters, planets
