"Schema for forecast query."

from typing import List


COLUMNS: List[str] = [
    "station",
    "datetime",
    "temperature",
    "wind_direction",
    "wind_speed",
    "precipitation",
    "forecast_date",
]
