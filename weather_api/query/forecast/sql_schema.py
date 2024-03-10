from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import (
    Station,
    Datetime,
    Temperature,
    WindSpeed,
    WindDirection,
    Precipitation,
)
from weather_api.data_catalog.sql_base import Base


class Forecast(Base):
    """Mapped class for forecast query."""

    __tablename__ = "forecast"

    station: Mapped[Station] = mapped_column(primary_key=True)
    datetime: Mapped[Datetime] = mapped_column(primary_key=True)
    temperature: Mapped[Temperature | None]
    wind_speed: Mapped[WindSpeed | None]
    wind_direction: Mapped[WindDirection | None]
    precipitation: Mapped[Precipitation | None]
    forecast_date: Mapped[Datetime] = mapped_column(primary_key=True)
