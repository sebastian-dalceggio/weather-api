"Module with SolarRadiation class that implements Query abstract class."

from typing import IO, Any

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern


class SolarRadiation(Query):
    """Class for measured query."""

    query: str = "solar_radiation"
    encoding: str = "us-ascii"

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(1):
            if not check_positional_line(cls.query, "headers", lines[i], i):
                raise NotExpectedPositionalLine(lines[i], i)
        iterator = iter(lines[1:])
        for line in iterator:
            if not check_line(cls.query, line, "data", date):
                raise NotExpectedPattern(line)
