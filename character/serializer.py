import uuid

from polaris.common.serializers import AuditorySerializer
from rest_framework import serializers

from character.models import CharacterModel


class CharacterSerializer(AuditorySerializer):
    char_id = serializers.UUIDField(required=False, default=uuid.uuid4, read_only=True)
    char_name = serializers.CharField(required=True)
    char_planet_home = serializers.CharField(required=True)
    char_planet_id = serializers.UUIDField(required=True)
    char_species = serializers.CharField(required=True)

    class Meta:
        model = CharacterModel
        fields = '__all__'

    @staticmethod
    def get_character(char_id):
        try:
            return CharacterModel.objects.get(char_id=char_id)
        except CharacterModel.DoesNotExist:
            return []
