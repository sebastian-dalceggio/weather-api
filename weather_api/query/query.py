"Module with the abstract class Query that is used as a blue print for all the ETL process."

from typing import IO, Any, List, Type
from abc import ABC, abstractmethod

import pandas as pd
import pandera as pa

from weather_api.download.smn_download import download_data


class Query(ABC):
    """Abstract class with the structure that any query must follow to be used in the ETL
    process."""

    QUERY: str = "base_class"
    ENCODING: str = "iso-8859-1"
    PA_SCHEMA: Type[pa.DataFrameModel] = pa.DataFrameModel

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
        encoding = cls.ENCODING if encode else None
        return download_data(cls.QUERY, date, encoding)

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
        # @pa.check_types
        # def _do_get_dataframe(cls, date: str, lines: List) ->
        #   pa.typing.DataFrame[pa.DataFrameModel]:
        # There is an open issue in Panderas about the same problem that I'm having on using
        # sublclases of DataFrameModel in the type hints. Because of it I will use validate method.
        # see: https://github.com/unionai-oss/pandera/issues/1170
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
        dataframe = cls.PA_SCHEMA.validate(dataframe)  # type: ignore[assignment]
        # dataframe = dataframe.astype(cls.PA_SCHEMA.to_schema().dtypes)  # type: ignore[arg-type]
        return dataframe

    @classmethod
    def validate_csv(cls, dataframe: pd.DataFrame, lazy: bool = True) -> None:
        """Validates the Pandas DataFrame

        Args:
            ddataframe (pd.DataFrame): Pandas DataFrame extracted from the csv data
            lazy (bool, optional): if True, lazily evaluates dataframe against all validation.
                Defaults to True.
        """
        cls.PA_SCHEMA.validate(dataframe, lazy=lazy)
