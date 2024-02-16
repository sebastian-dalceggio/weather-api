"Module with Observation class that implements Query abstract class."

from typing import IO, Any

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedHeader, NotExpectedLine


class Observations(Query):
    """Class for measured query."""

    query: str = "observations"
    encoding: str = "iso-8859-1"

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(3):
            if not check_positional_line(cls.query, "headers", lines[i], i):
                raise NotExpectedHeader(lines[i], i)
        iterator = iter(lines[3:])
        for line in iterator:
            if not check_line(cls.query, line, "data", date):
                raise NotExpectedLine(line)
