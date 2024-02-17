"Module with Forecast class that implements Query abstract class."

from typing import IO, Any

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern


class Forecast(Query):
    """Class for forecast query."""

    query: str = "forecast"
    encoding: str = "utf-8"

    @classmethod
    def validate_raw(  # pylint: disable=too-many-branches
        cls, date: str, file: IO[Any]
    ) -> None:
        lines = file.readlines()
        # checks if the first line is station or header
        if check_positional_line(cls.query, "headers", lines[0], 0):
            for i in range(5):
                if not check_positional_line(cls.query, "headers", lines[i], i):
                    raise NotExpectedPositionalLine(lines[i], i)
            iterator = iter(lines[5:])
        elif not check_line(cls.query, lines[0], "station"):
            raise NotExpectedPattern(lines[0])
        else:
            iterator = iter(lines)
        for line in iterator:
            if check_line(cls.query, line, "station"):
                for i in range(4):
                    next_line = next(iterator, "end_of_the_file")
                    if not check_positional_line(
                        cls.query, "inter_headers", next_line, i
                    ):
                        raise NotExpectedPositionalLine(next_line, i)
                next_line = next(iterator, "end_of_the_file")
                check_line(cls.query, next_line, "data", date)
                for i in range(39):
                    next_line = next(iterator, "end_of_the_file")
                    check = check_line(cls.query, next_line, "data", date)
                    if not check:
                        raise NotExpectedPattern(next_line)
                next_line = next(iterator, "end_of_the_file")
                check_end = check_positional_line(
                    cls.query, "inter_headers", next_line, 0
                )
                if not check_end:
                    raise NotExpectedPattern(next_line)
            else:
                raise NotExpectedPattern(line)
