from sqlalchemy.orm import Mapped, mapped_column

from weather_api.data_catalog.sql_typing import City, Datetime, Radiation
from weather_api.data_catalog.sql_base import Base


class SolarRadiation(Base):
    """Mapped class for solar_radiation query."""

    __tablename__ = "solar_radiation"

    city: Mapped[City] = mapped_column(primary_key=True)
    datetime: Mapped[Datetime] = mapped_column(primary_key=True)
    global_radiation: Mapped[Radiation | None]
    difuse_radiation: Mapped[Radiation | None]
