"Schema for measured query."

from weather_api.data_catalog.pandas_dtypes import (
    Station,
    Datetime,
    Temperature,
    WindSpeed,
    WindDirection,
    Humidity,
    Pressure,
    BaseSchema,
)

import pandera as pa


class MeasuredSchema(BaseSchema):
    """Measured Pandera schema"""

    datetime: Datetime
    temperature: Temperature = pa.Field(nullable=True)
    wind_speed: WindSpeed = pa.Field(nullable=True)
    wind_direction: WindDirection = pa.Field(nullable=True)
    humidity: Humidity = pa.Field(nullable=True)
    pressure: Pressure = pa.Field(nullable=True)
    station: Station

    class Config:
        unique = ["station", "datetime"]
