"Schema for forecast query."

import pandera as pa

from weather_api.data_catalog.column_type import (
    Station,
    Datetime,
    Temperature,
    WindSpeed,
    WindDirection,
    Precipitation,
    BaseSchema,
)


class ForecastSchema(BaseSchema):
    """Forecast Pandera schema"""

    station: Station
    datetime: Datetime
    temperature: Temperature = pa.Field(nullable=True)
    wind_speed: WindSpeed = pa.Field(nullable=True)
    wind_direction: WindDirection = pa.Field(nullable=True)
    precipitation: Precipitation = pa.Field(nullable=True)
    forecast_date: Datetime

    class Config:  # pylint: disable=too-few-public-methods
        """Schema config class"""

        unique = ["station", "datetime"]
