"Schema for observations query."

from weather_api.data_catalog.pandas_dtypes import (
    Station,
    Datetime,
    Temperature,
    BaseSchema,
)

import pandera as pa


class ObservationsSchema(BaseSchema):
    """Observations Pandera schema"""

    date: Datetime
    temperature_max: Temperature = pa.Field(nullable=True)
    temperature_min: Temperature = pa.Field(nullable=True)
    station: Station

    class Config:
        unique = ["station", "date"]
