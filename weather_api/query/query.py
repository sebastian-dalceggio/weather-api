"Module with the abstract class Query that is used as a blue print for all the ETL process."

from typing import IO, Any, List, Type
from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd
import pandera as pa
from cloudpathlib import CloudPath
from alembic.config import Config
from alembic import command
from alembic.util.exc import AutogenerateDiffsDetected
import sqlalchemy as sa

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

    @classmethod
    def run_database_migration(
        cls, database_uri: str, version_locations: Path | CloudPath
    ) -> None:
        """Read the table model and compare it with the current database model. If there is a
        difference between them, it generates the script to make the change and then runs it.

        Args:
            database_uri (str): database connection string.
        """
        alembic_cfg = Config()
        script_location = Path(__file__).parent.parent / "migrations"
        alembic_cfg.set_main_option("script_location", str(script_location))
        alembic_cfg.set_main_option("sqlalchemy.url", database_uri)
        alembic_cfg.set_main_option("version_locations", str(version_locations))
        try:
            command.check(alembic_cfg)
        except AutogenerateDiffsDetected:
            command.revision(alembic_cfg, autogenerate=True)
            command.upgrade(alembic_cfg, "head")
        else:
            print("No changes in the models detected.")

    @classmethod
    def load_to_database(
        cls, dataframe: pd.DataFrame, connection: sa.engine.Connection
    ) -> None:
        """Load the dataframe to the database.

        Args:
            dataframe (pd.DataFrame): dataframe to be loaded
            connection (sa.engine.Connection): connection to the database
        """
        dataframe = cls.PA_SCHEMA.validate(dataframe)  # type: ignore[assignment]
        dataframe.to_sql(cls.QUERY, connection, if_exists="append", index=False)
