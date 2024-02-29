"Schema for solar_radiation query."

from weather_api.data_catalog.pandas_dtypes import Radiation, Datetime, City, BaseSchema

import pandera as pa


class SolarRadiationSchema(BaseSchema):
    """Solar Radiation Pandera schema"""

    datetime: Datetime
    global_radiation: Radiation = pa.Field(nullable=True)
    difuse_radiation: Radiation = pa.Field(nullable=True)
    city: City

    class Config:
        unique = ["datetime", "city"]
