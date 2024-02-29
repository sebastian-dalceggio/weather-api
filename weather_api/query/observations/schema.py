"Schema for observations query."

import pandera as pa

from weather_api.data_catalog.column_type import (
    Station,
    Datetime,
    Temperature,
    BaseSchema,
)


class ObservationsSchema(BaseSchema):
    """Observations Pandera schema"""

    date: Datetime
    temperature_max: Temperature = pa.Field(nullable=True)
    temperature_min: Temperature = pa.Field(nullable=True)
    station: Station

    class Config:  # pylint: disable=too-few-public-methods
        """Schema config class"""

        unique = ["station", "date"]
