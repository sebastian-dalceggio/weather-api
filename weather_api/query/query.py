"Module with the abstract class Query that is used as a blue print for all the ETL process."

from typing import IO, Any, List
from abc import ABC, abstractmethod

import requests
import pandas as pd

from weather_api.download.smn_download import get_url_data
from weather_api.data_catalog import Schema


class Query(ABC):
    """Abstract class with the structure that any query must follow to be used in the ETL
    process."""

    QUERY: str = "base_class"
    ENCODING: str = "iso-8859-1"
    COLUMNS: List[str]

    @classmethod
    def schema(cls) -> Schema:
        """Returns the schema of the query.

        Returns:
            Schema: schema of the query
        """
        return Schema(cls.QUERY, cls.COLUMNS)

    @classmethod
    def download(cls, date: str, encode: bool = True) -> str:
        """Returns the requested daily data as text.

        Args:
            date (str): data required in the format YYYYMMDD.
            encode (bool, optional): if the response has to be encoded. Defaults to True.

        Raises:
            FileNotFoundError: if the file is not available in the source.

        Returns:
            str: response as a text.
        """

        url, file_does_not_exist_mssg = get_url_data(cls.QUERY, date)
        response = requests.get(url, timeout=60)
        if encode:
            response.encoding = cls.ENCODING
        text = response.text
        if text == file_does_not_exist_mssg:
            raise FileNotFoundError(file_does_not_exist_mssg)
        return text

    @classmethod
    @abstractmethod
    def validate_raw(cls, date: str, file: IO[Any]) -> None:
        """Validate the structure of a text file.

        Args:
            date (str): date required in the format YYYYMMDD.
            file (IO[Any]): open file with the text to validate.
        """

    @classmethod
    @abstractmethod
    def _do_get_dataframe(cls, date: str, lines: List) -> pd.DataFrame:
        """Do the actual transformation from the text file to the csv file.

        Args:
            date (str): date required in the format YYYYMMDD.
            lines (List): lines of the text file.

        Returns:
            pd.DataFrame: pandas dataframe extracted from the text file.
        """

    @classmethod
    def get_dataframe(cls, date: str, file_text: IO[Any]) -> pd.DataFrame:
        """Transforms the raw or cleaned file into a Pandas DataFrame. It also checks the structure
        of the data.

        Args:
            date (str): date required in the format YYYYMMDD.
            file_text (IO[Any]): text of the file.

        Returns:
            pd.DataFrame: pandas dataframe with the correct structure.
        """
        lines = file_text.readlines()
        dataframe = cls._do_get_dataframe(date, lines)
        dataframe.replace("", pd.NA, inplace=True)
        dataframe = dataframe.astype(cls.schema().dtypes)
        return dataframe
