from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import CityT, DatetimeT, RadiationT
from weather_api.data_catalog.sql_base import Base


class SolarRadiation(Base):
    """Mapped class for solar_radiation query."""

    __tablename__ = "solar_radiation"

    city: Mapped[CityT] = mapped_column(primary_key=True)
    datetime: Mapped[DatetimeT] = mapped_column(primary_key=True)
    global_radiation: Mapped[RadiationT | None]
    difuse_radiation: Mapped[RadiationT | None]
