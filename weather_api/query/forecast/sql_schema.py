from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import (
    StationT,
    DatetimeT,
    TemperatureT,
    WindSpeedT,
    WindDirectionT,
    PrecipitationT,
)
from weather_api.data_catalog.sql_base import Base


class Forecast(Base):
    """Mapped class for forecast query."""

    __tablename__ = "forecast"

    station: Mapped[StationT] = mapped_column(primary_key=True)
    datetime: Mapped[DatetimeT] = mapped_column(primary_key=True)
    temperature: Mapped[TemperatureT | None]
    wind_speed: Mapped[WindSpeedT | None]
    wind_direction: Mapped[WindDirectionT | None]
    precipitation: Mapped[PrecipitationT | None]
    forecast_date: Mapped[DatetimeT] = mapped_column(primary_key=True)
