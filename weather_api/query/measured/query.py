"Module with Measured class that implements Query abstract class."

from typing import IO, Any

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedHeader, NotExpectedLine


class Measured(Query):
    """Class for measured query."""

    query: str = "measured"
    encoding: str = "iso-8859-1"

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(2):
            if not check_positional_line(
                cls.query, "headers", lines[i], i
            ) and not check_positional_line(
                cls.query, "headers_alternative", lines[i], i
            ):
                raise NotExpectedHeader(lines[i], i)
        iterator = iter(lines[2:])
        current_pattern = "data"
        for line in iterator:
            if current_pattern == "empty":
                if not check_line(cls.query, line, "data", date):
                    raise NotExpectedLine(line)
                current_pattern = "data"
            elif current_pattern == "station":
                if not check_line(cls.query, line, "empty"):
                    raise NotExpectedLine(line)
                current_pattern = "empty"
            elif current_pattern == "data":
                if not check_line(cls.query, line, "data", date) and not check_line(
                    cls.query, line, "station"
                ):
                    raise NotExpectedLine(line)
                if check_line(cls.query, line, "data", date):
                    current_pattern = "data"
                else:
                    current_pattern = "station"
