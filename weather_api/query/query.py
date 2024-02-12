"Module with the abstract class Query that is used as a blue print for all the ETL process"

from typing import Optional
from abc import ABC, abstractmethod

import requests

from weather_api.download.smn_download import get_url_data


class Query(ABC):
    """Abstract class with the structure that any query must follow to be used in the ETL process.
    /"""

    query: str = "base_class"

    @classmethod
    def download(cls, date: str, encoding: Optional[str] = None) -> str:
        """Returns the requested daily data as text.

        Args:
            date (str): data required in the format YYYYMMDD
            enconding (Optional[str], optional): encoding use to read the data from the source.
                Defaults to None.

        Returns:
            str: response as a text
        """

        url, file_does_not_exist_mssg = get_url_data(cls.query, date)
        response = requests.get(url, timeout=60)
        if encoding:
            response.encoding = encoding
        text = response.text
        if text == file_does_not_exist_mssg:
            raise FileNotFoundError(file_does_not_exist_mssg)
        return text

    @classmethod
    @abstractmethod
    def validate(cls) -> None:
        """Validate the structure of the text file."""
