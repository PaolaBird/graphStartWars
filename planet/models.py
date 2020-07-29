import uuid

from cassandra.cqlengine import columns
from polaris.common.models import AuditoryModel


class PlanetModel(AuditoryModel):
    _table_name = "planet"
    plan_id = columns.UUID(required=True, primary_key=True, default=uuid.uuid4)
    plan_name = columns.Text(required=True)
    plan_weather = columns.Text(required=True)
    plan_location = columns.Text(required=True)

    class Meta:
        get_pk_field = 'plan_id'
