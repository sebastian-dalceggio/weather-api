from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import Station
from weather_api.data_catalog.sql_base import Base


class Stations(Base):
    """Mapped class for stations."""

    __tablename__ = "stations"

    station: Mapped[Station] = mapped_column(primary_key=True)
    measured_station: Mapped[Station | None] = mapped_column(primary_key=True)
    forecast_station: Mapped[Station | None] = mapped_column(primary_key=True)
    observation_station: Mapped[Station | None] = mapped_column(primary_key=True)
