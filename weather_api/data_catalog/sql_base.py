"Module with the base class for the mapped classes"

from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER, NUMERIC, TIMESTAMP

from weather_api.data_catalog.sql_typing import (
    Datetime,
    Temperature,
    Humidity,
    Pressure,
    WindDirection,
    WindSpeed,
    Precipitation,
    Station,
    City,
    Province,
    Radiation,
)


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class used to create all table classes."""

    registry = registry(
        type_annotation_map={
            Datetime: TIMESTAMP(True),
            Temperature: NUMERIC(3, 1),
            Humidity: INTEGER,
            Pressure: NUMERIC(5, 1),
            WindDirection: INTEGER,
            WindSpeed: NUMERIC(4, 1),
            Precipitation: NUMERIC(4, 1),
            Station: VARCHAR,
            City: VARCHAR,
            Province: VARCHAR,
            Radiation: NUMERIC(7, 3),
        }
    )
