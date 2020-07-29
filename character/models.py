import uuid

from cassandra.cqlengine import columns
from polaris.common.models import AuditoryModel


class CharacterModel(AuditoryModel):
    _table_name = "character"
    char_id = columns.UUID(required=True, primary_key=True, default=uuid.uuid4)
    char_name = columns.Text(required=True)
    char_planet_home = columns.Text(required=True)
    char_planet_id = columns.UUID(required=True)
    char_species = columns.Text(required=True)

    class Meta:
        get_pk_field = 'char_id'
