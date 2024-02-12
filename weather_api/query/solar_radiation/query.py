"Module with SolarRadiation class that implements Query abstract class."

from weather_api.query.query import Query


class SolarRadiation(Query):
    """Class for measured query."""

    query: str = "solar_radiation"

    @classmethod
    def validate(cls) -> None:
        return super().validate()
