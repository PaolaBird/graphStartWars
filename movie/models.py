import uuid

from cassandra.cqlengine import columns
from polaris.common.models import AuditoryModel


class MovieModel(AuditoryModel):
    _table_name = "movie"
    movi_id = columns.UUID(required=True, primary_key=True, default=uuid.uuid4)
    movi_name = columns.Text(required=True)
    movi_opening_text = columns.Text(required=True)
    movi_character_id = columns.List(required=True, value_type=columns.UUID())
    movi_character = columns.List(required=False,
                                 value_type=columns.Map(key_type=columns.Text(), value_type=columns.Text()))
    movi_director = columns.List(required=True, value_type=columns.Text())
    movi_producers = columns.List(required=True, value_type=columns.Text())
    movi_soundtrack = columns.List(required=True, value_type=columns.Text())
    movi_premiere = columns.Date(required=True)
    movi_duration = columns.Time(required=True)
    movi_planet_id = columns.List(required=True, value_type=columns.UUID())
    movi_planet = columns.List(required=False,
                                  value_type=columns.Map(key_type=columns.Text(), value_type=columns.Text()))

    class Meta:
        get_pk_field = 'movi_id'
