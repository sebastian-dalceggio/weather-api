"Functions to validate the measured text file structure."

from weather_api.utils.date import invert_date
from weather_api.exceptions import WrongDateError


def check_date_measured(line: str, date: str) -> None:
    """Checks if the data within the file corresponds to the correct date.
    Input pattern: '06022024    11  29.6   71  1014.9  360   13     AEROPARQUE AERO...'
                   '06022024  35.0  24.4 BUENOS AIRES OBSERVATORIO...'

    Args:
        line (str): string extracted from the file
        date (str): date of the file in the format YYYYMMDD.

    Raises:
        WrongDateError
    """
    date_inverted = invert_date(date)
    if not line[:8] == date_inverted:
        raise WrongDateError(line, date_inverted)
