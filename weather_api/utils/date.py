"Utils functions to manipulate dates"
from typing import Dict

import pendulum

MONTHS_DICT: Dict[str, int] = {
    "ENE": 1,
    "FEB": 2,
    "MAR": 3,
    "ABR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AGO": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DIC": 12,
}

DAYS_DELAY: Dict[str, int] = {
    "measured": 1,
    "forecast": 0,
    "observations": 1,
    "solar_radiation": 1,
}


def invert_date(date: str) -> str:
    """Inverts the date from the format YYYYMMDD to DDMMYYYY.

    Args:
        date (str): date in the format YYYYMMDD

    Returns:
        str: date in the format DDMMYYYY
    """
    return date[6:8] + date[4:6] + date[:4]


def format_measured_datetime(
    datetime: str, tz: str = "America/Argentina/Buenos_Aires"
) -> pendulum.DateTime:
    """Returns a pendulum datetime object from a datetime string with the format DDMMYYY    HH.

    Args:
        datetime (str): date in the format "DDMMYYY    HH"
        tz (str, optional): the timezone of the datetime. Defaults to
            "America/Argentina/Buenos_Aires".

    Returns:
        pendulum.DateTime: pendulum datetime
    """
    year = int(datetime[4:8])
    month = int(datetime[2:4])
    day = int(datetime[:2])
    hour = int(datetime[12:14])
    return pendulum.datetime(year, month, day, hour, tz=tz)


def format_forecast_datetime(
    datetime: str, tz: str = "America/Argentina/Buenos_Aires"
) -> pendulum.DateTime:
    """Returns a pendulum datetime object from a datetime string with the format DD/MMM/YYYY HH,
    with the month in Spanish.

    Args:
        datetime (str): date in the format "DD/MMM/YYYY HH"
        tz (str, optional): the timezone of the datetime. Defaults to
            "America/Argentina/Buenos_Aires".

    Returns:
        pendulum.DateTime: pendulum datetime
    """
    year = int(datetime[7:11])
    month = MONTHS_DICT[datetime[3:6]]
    day = int(datetime[:2])
    hour = int(datetime[12:14])
    return pendulum.datetime(year, month, day, hour, tz=tz)


def format_solar_radiation_datetime(
    datetime: str, tz: str = "America/Argentina/Buenos_Aires"
) -> pendulum.DateTime:
    """Returns a pendulum datetime object from a datetime string with the format
    YYYY-MM-DD HH:mm:ss.

    Args:
        datetime (str): date in the format "YYYY-MM-DD HH:mm:ss"
        tz (str, optional): the timezone of the datetime. Defaults to
            "America/Argentina/Buenos_Aires".

    Returns:
        pendulum.DateTime: pendulum datetime
    """
    return pendulum.from_format(datetime, "YYYY-MM-DD HH:mm:ss", tz=tz)


def format_observations_date(date: str) -> pendulum.Date:
    """Returns a pendulum date object from a date string with the format DDMMYYYY.

    Args:
        date (str): date in the format "DDMMYYYY"

    Returns:
        pendulum.DateTime: pendulum date
    """
    return pendulum.from_format(date, "DDMMYYYY").date()


def get_pendulum_datetime(
    date: str, tz: str = "America/Argentina/Buenos_Aires"
) -> pendulum.DateTime:
    """Returns the a pendulum datetime object from a datetime string with the format "YYYYMMDD".

    Args:
        date (str): date in the format YYYYMMDD
        tz (str, optional): the timezone of the datetime. Defaults to
            "America/Argentina/Buenos_Aires".

    Returns:
        pendulum.DateTime: pendulum datetime
    """
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    return pendulum.datetime(year, month, day, tz=tz)


def get_str_date(query: str, date: str) -> str:
    """Gets the current date and returns the correspond date for each process. It takes into
    account the necessary day delay to obtain the correct data.

    Args:
        query (str), {"measured", "forecast"}: type of data required
        date (str): data_interval_end as airflow gives it in the format "YYYY-MM-DD HH:mm:ssZ"

    Returns:
        str: date in the format YYYYMMDD
    """
    days_delay = DAYS_DELAY[query]
    pendulum_date = pendulum.from_format(date, "YYYY-MM-DD HH:mm:ssZ")
    real_date = pendulum_date.subtract(days=days_delay)
    return real_date.format("YYYYMMDD")
