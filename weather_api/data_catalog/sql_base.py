"Module with the base class for the mapped classes"

from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER, NUMERIC, TIMESTAMP

from weather_api.data_catalog.sql_typing import (
    DatetimeT,
    TemperatureT,
    HumidityT,
    PressureT,
    WindDirectionT,
    WindSpeedT,
    PrecipitationT,
    StationT,
    CityT,
    ProvinceT,
    RadiationT,
)


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class used to create all table classes."""

    registry = registry(
        type_annotation_map={
            DatetimeT: TIMESTAMP(True),
            TemperatureT: NUMERIC(3, 1),
            HumidityT: INTEGER,
            PressureT: NUMERIC(5, 1),
            WindDirectionT: INTEGER,
            WindSpeedT: NUMERIC(4, 1),
            PrecipitationT: NUMERIC(4, 1),
            StationT: VARCHAR,
            CityT: VARCHAR,
            ProvinceT: VARCHAR,
            RadiationT: NUMERIC(7, 3),
        }
    )
