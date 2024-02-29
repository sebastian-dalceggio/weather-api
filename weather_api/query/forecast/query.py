"Module with Forecast class that implements Query abstract class."

from typing import IO, Any, List, Dict, Type

import pandas as pd
import pandera as pa

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern
from weather_api.utils.date import format_forecast_datetime, get_pendulum_datetime
from weather_api.query.forecast.schema import ForecastSchema


class Forecast(Query):
    """Class for forecast query."""

    QUERY: str = "forecast"
    ENCODING: str = "utf-8"
    PA_SCHEMA: Type[pa.DataFrameModel] = ForecastSchema

    @classmethod
    def validate_raw(  # pylint: disable=too-many-branches
        cls, date: str, file: IO[Any]
    ) -> None:
        lines = file.readlines()
        # checks if the first line is station or header
        if check_positional_line(cls.QUERY, "headers", lines[0], 0):
            for i in range(5):
                if not check_positional_line(cls.QUERY, "headers", lines[i], i):
                    raise NotExpectedPositionalLine(lines[i], i)
            iterator = iter(lines[5:])
        elif not check_line(cls.QUERY, lines[0], "station"):
            raise NotExpectedPattern(lines[0])
        else:
            iterator = iter(lines)
        for line in iterator:
            if check_line(cls.QUERY, line, "station"):
                for i in range(4):
                    next_line = next(iterator, "end_of_the_file")
                    if not check_positional_line(
                        cls.QUERY, "inter_headers", next_line, i
                    ):
                        raise NotExpectedPositionalLine(next_line, i)
                next_line = next(iterator, "end_of_the_file")
                check_line(cls.QUERY, next_line, "data", date)
                for i in range(39):
                    next_line = next(iterator, "end_of_the_file")
                    check = check_line(cls.QUERY, next_line, "data", date)
                    if not check:
                        raise NotExpectedPattern(next_line)
                next_line = next(iterator, "end_of_the_file")
                check_end = check_positional_line(
                    cls.QUERY, "inter_headers", next_line, 0
                )
                if not check_end:
                    raise NotExpectedPattern(next_line)
            else:
                raise NotExpectedPattern(line)

    @classmethod
    def _do_get_dataframe(cls, date: str, lines: List) -> pd.DataFrame:
        rows = []
        current_station = ""
        for _, line in enumerate(lines):
            if any(
                check_positional_line(cls.QUERY, "headers", line, i) for i in range(5)
            ):
                continue
            if any(
                check_positional_line(cls.QUERY, "inter_headers", line, i)
                for i in range(4)
            ):
                continue
            if check_line(cls.QUERY, line, "station"):
                current_station = line.strip()
            else:
                current_dict: Dict[str, Any] = {}
                current_dict["station"] = current_station
                current_dict["datetime"] = format_forecast_datetime(line[1:15])
                current_dict["temperature"] = line[25:30].strip()
                current_dict["wind_direction"] = line[37:40].strip()
                current_dict["wind_speed"] = line[43:46].strip()
                current_dict["precipitation"] = line[53:58].strip()
                current_dict["forecast_date"] = get_pendulum_datetime(date).date()
                rows.append(current_dict)
        return pd.DataFrame(rows)
