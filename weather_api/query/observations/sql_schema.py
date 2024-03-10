from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import StationT, DatetimeT, TemperatureT
from weather_api.data_catalog.sql_base import Base


class Observations(Base):
    """Mapped class for observations query."""

    __tablename__ = "observations"

    station: Mapped[StationT] = mapped_column(primary_key=True)
    date: Mapped[DatetimeT] = mapped_column(primary_key=True)
    temperature_max: Mapped[TemperatureT | None]
    temperature_min: Mapped[TemperatureT | None]
