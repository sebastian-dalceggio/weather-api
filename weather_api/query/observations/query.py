"Module with Observation class that implements Query abstract class."

from typing import IO, Any, List, Dict, Type

import pandas as pd
import pandera as pa

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern
from weather_api.utils.date import format_observations_date
from weather_api.query.observations.schema import ObservationsSchema


class Observations(Query):
    """Class for observations query."""

    QUERY: str = "observations"
    ENCODING: str = "iso-8859-1"
    PA_SCHEMA: Type[pa.DataFrameModel] = ObservationsSchema

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(3):
            if not check_positional_line(cls.QUERY, "headers", lines[i], i):
                raise NotExpectedPositionalLine(lines[i], i)
        iterator = iter(lines[3:])
        for line in iterator:
            if not check_line(cls.QUERY, line, "data", date):
                raise NotExpectedPattern(line)

    @classmethod
    def _do_get_dataframe(cls, date: str, lines: List) -> pd.DataFrame:
        rows = []
        rows_to_filter = [0, 1, 2]
        for pos, line in enumerate(lines):
            current_dict: Dict[str, Any] = {}
            if pos in rows_to_filter:
                continue
            current_date = line[:8]
            current_dict["date"] = format_observations_date(current_date)
            current_dict["temperature_max"] = line[9:15].strip()
            current_dict["temperature_min"] = line[15:21].strip()
            current_dict["station"] = line[21:].strip()
            rows.append(current_dict)
        return pd.DataFrame(rows)
