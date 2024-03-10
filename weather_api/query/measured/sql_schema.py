from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import (
    Station,
    Datetime,
    Temperature,
    WindSpeed,
    WindDirection,
    Humidity,
    Pressure,
)
from weather_api.data_catalog.sql_base import Base


class Measured(Base):
    """Mapped class for measured query."""

    __tablename__ = "measured"

    station: Mapped[Station] = mapped_column(primary_key=True)
    datetime: Mapped[Datetime] = mapped_column(primary_key=True)
    temperature: Mapped[Temperature | None]
    wind_speed: Mapped[WindSpeed | None]
    wind_direction: Mapped[WindDirection | None]
    humidity: Mapped[Humidity | None]
    pressure: Mapped[Pressure | None]
