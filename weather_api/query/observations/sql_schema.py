from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import Station, Datetime, Temperature
from weather_api.data_catalog.sql_base import Base


class Observations(Base):
    """Mapped class for observations query."""

    __tablename__ = "observations"

    station: Mapped[Station] = mapped_column(primary_key=True)
    date: Mapped[Datetime] = mapped_column(primary_key=True)
    temperature_max: Mapped[Temperature | None]
    temperature_min: Mapped[Temperature | None]
