"Functions to validate the solar_radiation text file structure."

from weather_api.exceptions import WrongDateError


def check_date_solar_radiation(line: str, date: str) -> None:
    """Checks if the data within the file corresponds to the correct date.
    Input pattern: '2024-02-06 00:18:00,-1.736,-1.392,5.823,4.204'

    Args:
        line (str): string extracted from the file
        date (str): date of the file in the format YYYYMMDD.

    Raises:
        WrongDateError
    """
    if not line[:10].replace("-", "") == date:
        raise WrongDateError(line, date)
