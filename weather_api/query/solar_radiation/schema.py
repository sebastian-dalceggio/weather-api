"Schema for solar_radiation query."

import pandera as pa

from weather_api.data_catalog.column_type import Radiation, Datetime, City, BaseSchema


class SolarRadiationSchema(BaseSchema):
    """Solar Radiation Pandera schema"""

    datetime: Datetime
    global_radiation: Radiation = pa.Field(nullable=True)
    difuse_radiation: Radiation = pa.Field(nullable=True)
    city: City

    class Config:  # pylint: disable=too-few-public-methods
        """Schema config class"""

        unique = ["datetime", "city"]
