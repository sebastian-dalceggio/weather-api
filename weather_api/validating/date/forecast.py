"Functions to validate the forecast text file structure."

from weather_api.exceptions import WrongDateError
from weather_api.utils.date import (
    format_forecast_datetime,
    get_pendulum_datetime,
)


def check_date_forecast(line: str, date: str) -> None:
    """Checks if the data within the file corresponds to the correct date.
    The forecast file has data from the current day to the next five days.
    Input pattern: '07/FEB/2024 09Hs.        30.3       347 |  15         0.0 '

    Args:
        line (str): string extracted from the file
        date (str): date of the file in the format YYYYMMDD.

    Raises:
        WrongDateError
    """
    extract_date = line[1:17]
    date_in_file = format_forecast_datetime(extract_date).date()
    required_date = get_pendulum_datetime(date).date()
    difference = required_date.diff(date_in_file, abs=False).in_days()
    if difference >= 5 or difference < 0:
        raise WrongDateError(line, date)
