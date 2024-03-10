from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import Station
from weather_api.data_catalog.sql_base import Base


class Stations(Base):
    """Mapped class for stations."""

    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(primary_key=True)
    station: Mapped[Station]
    measured_station: Mapped[Station | None]
    forecast_station: Mapped[Station | None]
    observation_station: Mapped[Station | None]
    comments: Mapped[str | None]
