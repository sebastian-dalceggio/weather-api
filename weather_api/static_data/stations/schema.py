"Schema for stations."

import pandera as pa

from weather_api.data_catalog.pandas_types import (
    Station,
    BaseSchema,
)


class StationSchema(BaseSchema):
    """Forecast Pandera schema"""

    id: int = pa.Field(unique=True)
    station: Station
    measured_station: Station = pa.Field(nullable=True)
    forecast_station: Station = pa.Field(nullable=True)
    observation_station: Station = pa.Field(nullable=True)
