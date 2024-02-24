"Module with SolarRadiation class that implements Query abstract class."

from typing import IO, Any, List, Dict

import pandas as pd

from weather_api.query.query import Query
from weather_api.validating import check_line, check_positional_line
from weather_api.exceptions import NotExpectedPositionalLine, NotExpectedPattern
from weather_api.utils.date import format_solar_radiation_datetime
from weather_api.query.solar_radiation.schema import COLUMNS


class SolarRadiation(Query):
    """Class for solar_radiation query."""

    QUERY: str = "solar_radiation"
    ENCODING: str = "us-ascii"
    COLUMNS: List[str] = COLUMNS

    @classmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        lines = file.readlines()
        for i in range(1):
            if not check_positional_line(cls.QUERY, "headers", lines[i], i):
                raise NotExpectedPositionalLine(lines[i], i)
        iterator = iter(lines[1:])
        for line in iterator:
            if not check_line(cls.QUERY, line, "data", date):
                raise NotExpectedPattern(line)

    @classmethod
    def _do_get_dataframe(cls, date: str, lines: List) -> pd.DataFrame:
        rows = []
        rows_to_filter = [0]
        for pos, line in enumerate(lines):
            current_dict_ba: Dict[str, Any] = {}
            current_dict_us: Dict[str, Any] = {}
            if pos in rows_to_filter:
                continue
            data = line.split(",")
            current_datetime = format_solar_radiation_datetime(data[0])

            # Buenos Aires
            current_dict_ba["datetime"] = current_datetime
            current_dict_ba["city"] = "Buenos Aires"
            current_dict_ba["global_radiation"] = data[1]
            current_dict_ba["difuse_radiation"] = data[2]
            rows.append(current_dict_ba)

            # Ushuaia
            current_dict_us["datetime"] = current_datetime
            current_dict_us["city"] = "Ushuaia"
            current_dict_us["global_radiation"] = data[3]
            current_dict_us["difuse_radiation"] = data[4]
            rows.append(current_dict_us)
        return pd.DataFrame(rows)
