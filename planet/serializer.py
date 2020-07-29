import uuid

from polaris.common.serializers import AuditorySerializer
from rest_framework import serializers

from planet.models import PlanetModel


class PlanetSerializer(AuditorySerializer):
    plan_id = serializers.UUIDField(required=False, default=uuid.uuid4, read_only=True)
    plan_name = serializers.CharField(required=True)
    plan_weather = serializers.CharField(required=False)
    plan_location = serializers.CharField(required=False)

    class Meta:
        model = PlanetModel
        fields = '__all__'

    @staticmethod
    def get_planet(plan_id):
        try:
            return PlanetModel.objects.get(plan_id=plan_id)
        except PlanetModel.DoesNotExist:
            return []