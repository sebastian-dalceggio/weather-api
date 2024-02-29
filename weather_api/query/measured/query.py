"Module with Measured class that implements Query abstract class."

from typing import IO, Any, List, Dict, Type

import pandas as pd
import pandera as pa

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern
from weather_api.utils.date import format_measured_datetime
from weather_api.query.measured.schema import MeasuredSchema


class Measured(Query):
    """Class for measured query."""

    QUERY: str = "measured"
    ENCODING: str = "iso-8859-1"
    PA_SCHEMA: Type[pa.DataFrameModel] = MeasuredSchema

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(2):
            if not check_positional_line(
                cls.QUERY, "headers", lines[i], i
            ) and not check_positional_line(
                cls.QUERY, "headers_alternative", lines[i], i
            ):
                raise NotExpectedPositionalLine(lines[i], i)
        iterator = iter(lines[2:])
        current_pattern = "data"
        for line in iterator:
            if current_pattern == "empty":
                if not check_line(cls.QUERY, line, "data", date):
                    raise NotExpectedPattern(line)
                current_pattern = "data"
            elif current_pattern == "station":
                if not check_line(cls.QUERY, line, "empty"):
                    raise NotExpectedPattern(line)
                current_pattern = "empty"
            elif current_pattern == "data":
                if not check_line(cls.QUERY, line, "data", date) and not check_line(
                    cls.QUERY, line, "station"
                ):
                    raise NotExpectedPattern(line)
                if check_line(cls.QUERY, line, "data", date):
                    current_pattern = "data"
                else:
                    current_pattern = "station"

    @classmethod
    def _do_get_dataframe(cls, date: str, lines: List) -> pd.DataFrame:
        rows = []
        rows_to_filter = [0, 1]
        for pos, line in enumerate(lines):
            current_dict: Dict[str, Any] = {}
            if pos in rows_to_filter:
                continue
            if check_line(cls.QUERY, line, "station") or check_line(
                cls.QUERY, line, "empty"
            ):
                continue
            current_datetime = line[:15]
            current_dict["datetime"] = format_measured_datetime(current_datetime)
            current_dict["temperature"] = line[15:21].strip()
            current_dict["humidity"] = line[22:25].strip()
            current_dict["pressure"] = line[27:34].strip()
            current_dict["wind_direction"] = line[35:39].strip()
            current_dict["wind_speed"] = line[40:45].strip()
            current_dict["station"] = line[46:].strip()
            rows.append(current_dict)
        return pd.DataFrame(rows)
