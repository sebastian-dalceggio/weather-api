"Module with Observation class that implements Query abstract class."

from weather_api.query.query import Query


class Observations(Query):
    """Class for measured query."""

    query: str = "observations"

    @classmethod
    def validate(cls) -> None:
        return super().validate()
