"Functions used to download data from https://www.smn.gob.ar/descarga-de-datos"

from typing import Optional
from pathlib import Path

import requests

from weather_api.utils.files import get_json_data

current_directory = Path(__file__).resolve().parent

QUERY_DATA_FILE = current_directory / "smn_urls.json"


def _get_query_data(query: str, data: str, date: str) -> str:
    """Gets the url or file not exist text for each query for a specific date.

    Args:
        query (str), {"measured", "forecast"}: type of data required
        data (str), {"url", "not exist"}: data required
        date (str): data required in the format YYYYMMDD

    Returns:
        str: the data as a text
    """
    values_dict = get_json_data(QUERY_DATA_FILE, {"query_date": date})[query]
    return values_dict[data]


def get_smn_daily_data(query: str, date: str, encoding: Optional[str] = None) -> str:
    """Returns the requested daily data as text.

    Args:
        query (str): type of data requested
        date (str): data required in the format YYYYMMDD
        enconding (Optional[str], optional): encoding use to read the data from the source.
            Defaults to None.

    Returns:
        str: response as a text
    """
    url = _get_query_data(query, "url", date)
    file_does_not_exist_mssg = _get_query_data(query, "not exist", date)
    response = requests.get(url, timeout=60)
    if encoding:
        response.encoding = encoding
    text = response.text
    if text == file_does_not_exist_mssg:
        raise FileNotFoundError(file_does_not_exist_mssg)
    return text
