"Patterns for all the queries"

from typing import Dict

from weather_api.validating.patterns.regex_data import (
    MEASURED_REGEX_PATTERNS,
    FORECAST_REGEX_PATTERNS,
    OBSERVATIONS_REGEX_PATTERNS,
    SOLAR_RADIATION_REGEX_PATTERNS,
)

REGEX_PATTERNS: Dict[str, Dict[str, str]] = {
    "measured": MEASURED_REGEX_PATTERNS,
    "forecast": FORECAST_REGEX_PATTERNS,
    "observations": OBSERVATIONS_REGEX_PATTERNS,
    "solar_radiation": SOLAR_RADIATION_REGEX_PATTERNS,
}
