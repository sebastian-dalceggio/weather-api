"Module with the abstract class Query that is used as a blue print for all the ETL process"

from typing import IO, Any
from abc import ABC, abstractmethod

import requests

from weather_api.download.smn_download import get_url_data


class Query(ABC):
    """Abstract class with the structure that any query must follow to be used in the ETL
    process."""

    query: str = "base_class"
    encoding: str = "iso-8859-1"

    @classmethod
    def download(cls, date: str, encode: bool = True) -> str:
        """Returns the requested daily data as text.

        Args:
            date (str): data required in the format YYYYMMDD

        Returns:
            str: response as a text
        """

        url, file_does_not_exist_mssg = get_url_data(cls.query, date)
        response = requests.get(url, timeout=60)
        if encode:
            response.encoding = cls.encoding
        text = response.text
        if text == file_does_not_exist_mssg:
            raise FileNotFoundError(file_does_not_exist_mssg)
        return text

    @classmethod
    @abstractmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        """Validate the structure of a text file.

        Args:
            date (str): date required in the format YYYYMMDD
            file (IO[Any]): open file with the text to validate
        """
