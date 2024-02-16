"Utils for validation"

from typing import Dict, Callable
from weather_api.validating.date.measured import check_date_measured
from weather_api.validating.date.forecast import check_date_forecast
from weather_api.validating.date.solar_radiation import check_date_solar_radiation

CHECK_DATE_DICT: Dict[str, Callable] = {
    "measured": check_date_measured,
    "forecast": check_date_forecast,
    "observations": check_date_measured,
    "solar_radiation": check_date_solar_radiation,
}
