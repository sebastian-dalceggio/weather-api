from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import (
    StationT,
    DatetimeT,
    TemperatureT,
    WindSpeedT,
    WindDirectionT,
    HumidityT,
    PressureT,
)
from weather_api.data_catalog.sql_base import Base


class Measured(Base):
    """Mapped class for measured query."""

    __tablename__ = "measured"

    station: Mapped[StationT] = mapped_column(primary_key=True)
    datetime: Mapped[DatetimeT] = mapped_column(primary_key=True)
    temperature: Mapped[TemperatureT | None]
    wind_speed: Mapped[WindSpeedT | None]
    wind_direction: Mapped[WindDirectionT | None]
    humidity: Mapped[HumidityT | None]
    pressure: Mapped[PressureT | None]
