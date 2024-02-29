"Schema for forecast query."

from weather_api.data_catalog.pandas_dtypes import (
    Station,
    Datetime,
    Temperature,
    WindSpeed,
    WindDirection,
    Precipitation,
    BaseSchema,
)

import pandera as pa


class ForecastSchema(BaseSchema):
    """Forecast Pandera schema"""

    station: Station
    datetime: Datetime
    temperature: Temperature = pa.Field(nullable=True)
    wind_speed: WindSpeed = pa.Field(nullable=True)
    wind_direction: WindDirection = pa.Field(nullable=True)
    precipitation: Precipitation = pa.Field(nullable=True)
    forecast_date: Datetime

    class Config:
        unique = ["station", "datetime"]
