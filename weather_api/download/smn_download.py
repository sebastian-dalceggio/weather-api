"Functions used to download data from https://www.smn.gob.ar/descarga-de-datos"

from typing import Tuple
from pathlib import Path

from weather_api.utils.files import get_yaml_data

current_directory = Path(__file__).resolve().parent

QUERY_DATA_FILE = current_directory / "url_data.yaml"


def get_url_data(query: str, date: str) -> Tuple[str, str]:
    """Gets the url or file not exist text for each query for a specific date.

    Args:
        query (str), {"measured", "forecast"}: type of data required
        date (str): data required in the format YYYYMMDD

    Returns:
        str: the data as a text
    """
    values_dict = get_yaml_data(QUERY_DATA_FILE, {"query_date": date})[query]
    return values_dict["url"], values_dict["not exist"]
