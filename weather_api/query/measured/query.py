"Module with Measured class that implements Query abstract class."

from weather_api.query.query import Query


class Measured(Query):
    """Class for measured query."""

    query: str = "measured"

    @classmethod
    def validate(cls) -> None:
        return super().validate()
