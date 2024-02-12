"Module with Forecast class that implements Query abstract class."

from weather_api.query.query import Query


class Forecast(Query):
    """Class for forecast query."""

    query: str = "forecast"

    @classmethod
    def validate(cls) -> None:
        return super().validate()
