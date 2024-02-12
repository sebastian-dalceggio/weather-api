"Dict that matches the query string with the correct Query Class"

from typing import Dict, Type

from weather_api.query.query import Query
from weather_api.query.forecast.query import Forecast
from weather_api.query.measured.query import Measured
from weather_api.query.solar_radiation.query import SolarRadiation
from weather_api.query.observations.query import Observations

QUERY_DICT: Dict[str, Type[Query]] = {
    "forecast": Forecast,
    "measured": Measured,
    "solar_radiation": SolarRadiation,
    "observations": Observations,
}
