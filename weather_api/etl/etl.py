"""Actual functions that Airflow will import to run the ETL process. They translate the query name
into the specfic class while hundle the files."""

from typing import Optional
from pathlib import Path

from cloudpathlib import CloudPath
import pandas as pd
import sqlalchemy as sa

from weather_api.query import QUERY_DICT, Query
from weather_api.static_data import STATIC_DICT


def download(
    query: str,
    date: str,
    raw_file_path: Path | CloudPath,
    replace: Optional[bool] = False,
    encode: bool = True,
) -> bool:
    """Downloads the required data from SMN web and save it in the raw_file_path

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        date (str): date required in the format YYYYMMDD
        raw_file_path (Union[Path, CloudPath]): path where the data will be saved
        replace (Optional[bool], optional): If True the file the file will be createad again if it
            already exists. Defaults to False.

    Returns:
        bool: True if the file was downloaded, False if it already exists
    """
    if replace or not raw_file_path.exists():
        query_class = QUERY_DICT[query]
        content = query_class.download(date, encode=encode)
        raw_file_path.parent.mkdir(parents=True, exist_ok=True)
        raw_file_path.write_text(content, encoding=query_class.ENCODING)
        return True
    print(f"File {raw_file_path.as_uri()} already exists.")
    return False


def validate_raw(query: str, date: str, raw_file_path: Path | CloudPath) -> None:
    """Validate that the raws data follows te established pattern.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
            required
        date (str): date required in the format YYYYMMDD
        raw_file_path (Union[Path, CloudPath]): path where the data was saved
    """
    query_class = QUERY_DICT[query]
    with raw_file_path.open("r", encoding=query_class.ENCODING) as raw_file:
        query_class.validate_raw(date, raw_file)


def to_csv(
    query: str,
    date: str,
    text_file_path: Path | CloudPath,
    csv_file_path: Path | CloudPath,
    replace: Optional[bool] = False,
) -> None:
    """Transforms the text file into a csv file.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
        date (str): date required in the format YYYYMMDD
        text_file_path (Union[Path, CloudPath]): path to the text file
        csv_file_path (Union[Path, CloudPath]): path where the csv file will be saved
        replace (Optional[bool], optional): If True the file the file will be createad againg if it
            already exists. Defaults to False.
    """
    if not csv_file_path.exists() or replace:
        query_class = QUERY_DICT[query]
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        with text_file_path.open("r", encoding=query_class.ENCODING) as file_text:
            dataframe = query_class.get_dataframe(date, file_text)
            dataframe.to_csv(
                str(csv_file_path), index=False, encoding=query_class.ENCODING
            )
    else:
        print(f"File {csv_file_path.as_uri()} already exists.")


def migrate_database(database_uri: str, version_locations: Path | CloudPath) -> None:
    """Validates the structure of the csv file

    Args:
        database_uri (str): uri of the database
        version_location (Union[Path, CloudPath]): folder where the versions will be saved
    """
    Query.run_database_migration(database_uri, version_locations)


def to_database(query: str, csv_file_path: Path | CloudPath, database_uri: str) -> None:
    """Loads the query table to the database.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data
        csv_file_path (Union[Path, CloudPath]): path to the csv file
        database_uri (str): uri of the database
    """
    query_class = QUERY_DICT[query]
    dataframe = pd.read_csv(str(csv_file_path), encoding=query_class.ENCODING)
    engine = sa.create_engine(database_uri)
    with engine.connect() as connection:
        query_class.load_to_database(dataframe, connection)


def check_to_database(
    query: str, date: str, data_source_name: str, configuration_file_path: Path
) -> None:
    """Data validation on the query tables using Soda.

    Args:
        query (str), {"measured", "forecast", "observations", "solar_radiation"}: type of data.
        date (str): date required in the format YYYYMMDD.
        data_source_name (str): data source name.
        configuration_file_path (Path): path to the datasource configuration path.
    """
    query_class = QUERY_DICT[query]
    query_class.check_load_to_database(date, data_source_name, configuration_file_path)


def load_static_data(static_data: str, database_uri: str) -> None:
    """Load static data into the database.

    Args:
        static_data (str), {"stations"}: type of data.
        database_uri (str): uri of the database
    """
    static_data_type = STATIC_DICT[static_data]
    static_data_type(database_uri)
